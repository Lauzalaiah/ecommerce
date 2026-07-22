# Automatisation réseaux sociaux — le plus proche d'un "agent" légitime

Ce que fait réellement ce dossier : publier automatiquement, 3 fois par semaine (lundi/mercredi/vendredi 9h UTC), le prochain post de `content_calendar.json` sur ta Page Facebook (et sur Instagram si une photo est renseignée) — sans que tu aies à t'en occuper une fois branché. C'est une automatisation légitime (le même principe que Buffer ou Meta Business Suite), pas un envoi de messages à des personnes : elle publie sur tes propres comptes publics, que les gens découvrent ou non de leur plein gré.

## Ce que je ne peux pas faire à ta place

Créer tes jetons d'accès (`FB_PAGE_ACCESS_TOKEN`, etc.) suppose de posséder et gérer ta Page Facebook/compte Instagram Business — une identité et des droits qui doivent rester les tiens. Ce qui suit prend 10-15 minutes, une seule fois.

## Mise en place (une fois)

1. **Convertir ton compte Instagram en compte professionnel** (Paramètres → Compte → Passer à un compte professionnel) et le lier à ta Page Facebook.
2. Sur [developers.facebook.com](https://developers.facebook.com) → **Mes apps** → **Créer une app** → type "Entreprise".
3. Dans l'app, ajoute le produit **Graph API Explorer** :
   - Sélectionne ta Page dans le menu déroulant "User or Page".
   - Génère un token avec les permissions `pages_manage_posts`, `pages_read_engagement`, `instagram_basic`, `instagram_content_publish`.
   - Ce token expire par défaut en 1h — échange-le contre un **token longue durée** (~60 jours) via l'outil "Access Token Debugger" de Meta, puis renouvelle-le à l'approche de l'expiration (Meta recommande cette pratique plutôt qu'un token permanent).
4. Récupère ton `FB_PAGE_ID` : visible dans **Paramètres de la Page → Informations sur la Page**, ou via `GET /me/accounts` dans Graph API Explorer.
5. Récupère ton `IG_BUSINESS_ACCOUNT_ID` : `GET /{FB_PAGE_ID}?fields=instagram_business_account` dans Graph API Explorer.

## Ajouter les secrets dans GitHub

Dans ce dépôt GitHub → **Settings → Secrets and variables → Actions → New repository secret**, ajoute :
- `FB_PAGE_ID`
- `FB_PAGE_ACCESS_TOKEN`
- `IG_BUSINESS_ACCOUNT_ID` (optionnel, seulement si tu veux aussi publier sur Instagram)

## Tester manuellement avant de laisser tourner seul

Onglet **Actions** du dépôt GitHub → workflow "Publication automatique réseaux sociaux" → **Run workflow** (bouton à droite) → vérifie sur ta Page que le post est bien apparu, puis supprime-le si c'était juste un test.

## Limite actuelle à connaître

Instagram exige une photo pour publier (pas de post texte seul) — tant que `image_url` est vide dans `content_calendar.json`, seul Facebook reçoit le post, Instagram est ignoré (le script te le signale dans les logs). Dès que tu as de vraies photos produit (voir `../marketing/supplier-sourcing-alibaba-guide.md`), héberge-les quelque part d'accessible publiquement (ex. une image déjà mise en ligne sur ta boutique Shopify) et ajoute l'URL dans le champ `image_url` du post correspondant.

## Ajuster le rythme ou le contenu

- Modifier/ajouter des posts : édite directement `content_calendar.json`.
- Changer la fréquence : modifie le `cron` dans `.github/workflows/social-auto-post.yml` (actuellement lundi/mercredi/vendredi) et `POST_INTERVAL_DAYS` dans `social_auto_poster.py` en conséquence.
- `EPOCH_DATE` dans `social_auto_poster.py` sert de point de départ au calcul — inutile d'y toucher sauf si tu veux forcer un post précis à une date donnée.
