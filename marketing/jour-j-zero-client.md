# Jour J : la boutique est prête, zéro client — quoi faire, dans quel ordre

Ce document assemble tout ce qui a été construit ailleurs (`launch-plan-30-60-90.md`, `strategie-sans-contenu-video.md`, `accelerer-acquisition-clients.md`, `automation/`) en une seule séquence à suivre mécaniquement le jour où la boutique est prête mais qu'il n'y a encore aucun client. Pas de nouvelle méthode ici, juste l'ordre exact d'exécution.

## Avant de commencer : vérifier que "prêt" veut vraiment dire prêt

- SIRET reçu (pas juste demandé).
- Thème en ligne, catalogue importé, au moins quelques vraies photos.
- Paiements actifs (Shopify Payments/Stripe) — fais toi-même un achat test avec une petite somme pour vérifier que le tunnel complet fonctionne (beaucoup de "zéro client" viennent en fait d'un panier cassé, pas d'un manque de visibilité).
- Pages légales publiées (mentions légales, CGV, confidentialité).

## Heures 1-4 : les leviers gratuits qui demandent seulement du temps

1. **Message personnel, pas un post** — écris individuellement à 15-20 proches ayant un chien/chat, demande explicitement un premier achat ou un avis (`launch-plan-30-60-90.md`, Jours 1-7). Le taux de conversion ici est sans comparaison avec n'importe quelle publicité.
2. **Lance `automation/prospect_finder.py`** avec ta ville → remplit `marketing/partner-outreach-tracker.csv` avec les vétos/toiletteurs/animaleries du coin.
3. **Envoie les 5 premiers messages** à ces contacts locaux (adapte `marketing/supplier-outreach-message.md` : catalogue → présentation + proposition de code de réduction en échange d'une mise en avant, comme prévu dans le tracker).

## Heures 4-8 : le levier argent, pour une visibilité immédiate

4. Admin Shopify → app **Google & YouTube** → connecte Google Merchant Center → synchronise le catalogue.
5. Lance une campagne **Shopping** à 5-10€/jour sur les mots-clés de besoin précis déjà listés (`seo-guide.md`, `strategie-sans-contenu-video.md`) — pas de mots génériques.
6. Vérifie que le Pixel Meta / tag Google sont posés (`accelerer-acquisition-clients.md` point 2) — sans ça, impossible de savoir ce qui marche ensuite.

## En parallèle, ça tourne déjà seul

- `automation/social_auto_poster.py` — publie 3x/semaine sans intervention (si les secrets Meta sont configurés).
- Séquences email (`email-flows.md`) — si déjà branchées dans Shopify Email.

## Jours 2-7 : observer, ne pas paniquer, ne pas tout changer d'un coup

- Regarde quotidiennement **Shopify Analytics** : d'où viennent les visites (réseaux, recherche, direct) ?
- Ne coupe aucune publicité avant 4-5 jours (protocole dans `ad-copy-templates.md`) — les premiers jours sont presque toujours plus chers, l'algorithme apprend.
- Relance une seule fois les contacts locaux qui n'ont pas répondu après 3-4 jours — pas plus, pour ne pas paraître insistant.

## Si après 7 jours c'est toujours zéro client

Dans cet ordre de vérification (le plus probable en premier) :
1. **Le tunnel d'achat fonctionne-t-il vraiment ?** Refais un achat test.
2. **Le message est-il assez précis ?** Un positionnement générique "bien-être" convertit moins qu'un problème précis nommé (`proposition-de-valeur.md`, `strategie-sans-contenu-video.md`) — vérifie que le hero et les fiches produit parlent d'un problème concret, pas d'un concept.
3. **Le budget pub cible-t-il une vraie recherche existante ?** Revoir les mots-clés avec le moins de concurrence mais une vraie intention d'achat.
4. **Élargir le rayon de prospection locale** — relance `prospect_finder.py` sur une ville/zone plus large.

Ce qui ne doit *pas* arriver à ce stade : tout changer en même temps (thème, prix, catalogue, canal) après seulement une semaine — ça rend impossible de savoir ce qui a marché ou pas la fois suivante.
