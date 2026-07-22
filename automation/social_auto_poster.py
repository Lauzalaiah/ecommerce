"""Publie automatiquement le prochain post du calendrier sur la Page Facebook
(et sur Instagram si une image_url est renseignée) via l'API Graph officielle.

Nécessite tes propres identifiants (voir automation/README.md) :
  FB_PAGE_ID              - identifiant de ta Page Facebook
  FB_PAGE_ACCESS_TOKEN    - jeton d'accès longue durée de cette Page
  IG_BUSINESS_ACCOUNT_ID  - identifiant de ton compte Instagram Business (optionnel)

Aucun message n'est jamais envoyé à un individu : ce script publie uniquement
sur tes propres comptes publics, comme le ferait Buffer ou Meta Business Suite.
"""
import json
import os
import sys
from datetime import date, datetime
from pathlib import Path

import requests

GRAPH_API_VERSION = "v19.0"
CALENDAR_PATH = Path(__file__).parent / "content_calendar.json"

# Date de référence du calendrier et intervalle entre deux posts (jours).
# Ajuste EPOCH_DATE à la date de ton premier post réel si besoin.
EPOCH_DATE = date(2026, 1, 5)
POST_INTERVAL_DAYS = 2


def pick_todays_post(posts: list[dict]) -> dict:
    days_elapsed = (date.today() - EPOCH_DATE).days
    index = (days_elapsed // POST_INTERVAL_DAYS) % len(posts)
    return posts[index]


def post_to_facebook_page(message: str, image_url: str, page_id: str, access_token: str) -> dict:
    if image_url:
        url = f"https://graph.facebook.com/{GRAPH_API_VERSION}/{page_id}/photos"
        payload = {"url": image_url, "caption": message, "access_token": access_token}
    else:
        url = f"https://graph.facebook.com/{GRAPH_API_VERSION}/{page_id}/feed"
        payload = {"message": message, "access_token": access_token}
    response = requests.post(url, data=payload, timeout=30)
    response.raise_for_status()
    return response.json()


def post_to_instagram(message: str, image_url: str, ig_account_id: str, access_token: str) -> dict:
    container_url = f"https://graph.facebook.com/{GRAPH_API_VERSION}/{ig_account_id}/media"
    container = requests.post(
        container_url,
        data={"image_url": image_url, "caption": message, "access_token": access_token},
        timeout=30,
    )
    container.raise_for_status()
    creation_id = container.json()["id"]

    publish_url = f"https://graph.facebook.com/{GRAPH_API_VERSION}/{ig_account_id}/media_publish"
    publish = requests.post(
        publish_url,
        data={"creation_id": creation_id, "access_token": access_token},
        timeout=30,
    )
    publish.raise_for_status()
    return publish.json()


def main() -> int:
    posts = json.loads(CALENDAR_PATH.read_text(encoding="utf-8"))
    post = pick_todays_post(posts)
    message = post["message"]
    image_url = post.get("image_url", "")

    page_id = os.environ.get("FB_PAGE_ID")
    page_token = os.environ.get("FB_PAGE_ACCESS_TOKEN")
    ig_account_id = os.environ.get("IG_BUSINESS_ACCOUNT_ID")

    if not page_id or not page_token:
        print("FB_PAGE_ID / FB_PAGE_ACCESS_TOKEN manquants — rien à publier. Voir automation/README.md.")
        return 1

    print(f"[{datetime.now().isoformat()}] Post #{post['id']} ({post['theme']})")

    fb_result = post_to_facebook_page(message, image_url, page_id, page_token)
    print("Facebook OK:", fb_result)

    if image_url and ig_account_id:
        ig_result = post_to_instagram(message, image_url, ig_account_id, page_token)
        print("Instagram OK:", ig_result)
    elif not image_url:
        print("Pas d'image_url pour ce post : Instagram ignoré (obligatoire côté Instagram).")

    return 0


if __name__ == "__main__":
    sys.exit(main())
