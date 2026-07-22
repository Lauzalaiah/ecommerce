"""Trouve automatiquement des partenaires locaux potentiels (vétérinaires,
toiletteurs, animaleries, éducateurs canins) via l'API Google Places, et les
ajoute à marketing/partner-outreach-tracker.csv.

C'est la version légitime d'un "agent qui trouve des clients" pour ce type de
commerce : il identifie des prospects publics (fiches d'entreprises), il ne
contacte personne automatiquement. L'envoi du message reste une action humaine
volontaire (voir marketing/supplier-outreach-message.md pour le modèle),
exactement comme le ferait un commercial qui se constitue une liste de
prospects avant de les appeler un par un.

Nécessite ta propre clé API Google Places (voir automation/README.md).
"""
import csv
import os
import sys
import time
from pathlib import Path

import requests

TRACKER_PATH = Path(__file__).parent.parent / "marketing" / "partner-outreach-tracker.csv"
FIELDNAMES = ["Nom", "Type", "Plateforme/Contact", "Statut", "Date dernier contact", "Prochaine action", "Notes"]

SEARCH_TYPES = {
    "vétérinaire": "Partenaire local (vétérinaire)",
    "toiletteur pour chien": "Partenaire local (toiletteur)",
    "animalerie": "Partenaire local (animalerie)",
    "éducateur canin": "Partenaire local (éducateur canin)",
}


def search_places(query: str, location: str, api_key: str) -> list[dict]:
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    response = requests.get(
        url, params={"query": f"{query} à {location}", "key": api_key}, timeout=30
    )
    response.raise_for_status()
    return response.json().get("results", [])


def place_details(place_id: str, api_key: str) -> dict:
    url = "https://maps.googleapis.com/maps/api/place/details/json"
    response = requests.get(
        url,
        params={"place_id": place_id, "fields": "formatted_phone_number,website", "key": api_key},
        timeout=30,
    )
    response.raise_for_status()
    return response.json().get("result", {})


def load_existing_names() -> set[str]:
    if not TRACKER_PATH.exists():
        return set()
    with TRACKER_PATH.open(newline="", encoding="utf-8") as f:
        return {row["Nom"].strip().lower() for row in csv.DictReader(f)}


def append_prospects(rows: list[dict]) -> None:
    file_exists = TRACKER_PATH.exists()
    with TRACKER_PATH.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        if not file_exists:
            writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    api_key = os.environ.get("GOOGLE_PLACES_API_KEY")
    location = os.environ.get("PROSPECT_CITY")

    if not api_key or not location:
        print("GOOGLE_PLACES_API_KEY et PROSPECT_CITY sont requis. Voir automation/README.md.")
        return 1

    existing = load_existing_names()
    new_rows = []

    for query, partner_type in SEARCH_TYPES.items():
        for place in search_places(query, location, api_key):
            name = place.get("name", "").strip()
            if not name or name.lower() in existing:
                continue

            details = place_details(place["place_id"], api_key)
            contact_parts = [p for p in [details.get("formatted_phone_number"), details.get("website")] if p]
            contact = " / ".join(contact_parts) or place.get("formatted_address", "")

            new_rows.append({
                "Nom": name,
                "Type": partner_type,
                "Plateforme/Contact": contact,
                "Statut": "A contacter",
                "Date dernier contact": "",
                "Prochaine action": "Proposer flyer + code de reduction en echange d'une mise en avant",
                "Notes": "Trouve automatiquement via prospect_finder.py",
            })
            existing.add(name.lower())
            time.sleep(0.2)

    if new_rows:
        append_prospects(new_rows)
    print(f"{len(new_rows)} nouveau(x) prospect(s) ajoute(s) a {TRACKER_PATH.name}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
