# PattesZen — Boutique en ligne bien-être animal (Shopify)

Ce dépôt contient tout ce qu'il faut pour relancer une boutique Shopify dédiée au bien-être animal (croquettes chien/chat, friandises, compléments, hygiène, accessoires), avec un objectif clair : **vendre plus vite que la dernière fois**, sans reproduire l'erreur de payer un abonnement Shopify avant d'avoir des clients.

**"PattesZen"** est un nom de marque provisoire — remplace-le partout par le tien en 5 minutes (voir `SETUP_GUIDE.md`).

## Ce qui est fourni ici

| Dossier | Contenu | Statut |
|---|---|---|
| `fast-start/` | Vendre en moins d'une heure (lien Stripe) + page de liste d'attente déjà en ligne | Prêt à l'emploi, déjà publié |
| `shopify-theme/` | Sections et templates Liquid (Online Store 2.0) à poser sur le thème gratuit Dawn | Prêt à l'emploi |
| `catalog/` | Catalogue produits (CSV) importable directement dans Shopify | Prêt à l'emploi, prix à ajuster |
| `marketing/` | Plan d'acquisition client, calendrier réseaux sociaux, pubs, emails, SEO, sourcing fournisseurs, message de reconnexion fournisseur | Prêt à l'emploi |
| `automation/` | Deux agents : publication auto 3x/semaine (Facebook/Instagram) + recherche automatique de prospects locaux (Google Places) | Prêt, à connecter à tes comptes |
| `SETUP_GUIDE.md` | Guide pas-à-pas pour tout brancher, du compte Shopify au premier client | À suivre dans l'ordre |

## Important, à lire avant de commencer

Je ne peux pas créer un compte Shopify à ta place, ni payer un abonnement, ni signer un contrat avec un fournisseur, ni faire de vraies ventes en ton nom — ce sont des actes commerciaux et financiers qui doivent rester entre tes mains (identité, moyens de paiement, responsabilité légale). Ce que j'ai fait à la place : **tout le travail préparatoire** (code, contenu, catalogue, plan d'action) pour que la partie qui reste à ta charge prenne le moins de temps possible.

Des outils se présentant comme des "agents IA" pour trouver des clients existent bel et bien (des plateformes comme blink.new permettent d'en construire) — mais ce qu'ils font concrètement, une fois qu'on regarde sous le capot, c'est de la recherche web, de la génération de contenu et parfois de l'emailing B2B automatisé : la même catégorie d'automatisation que `automation/` fournit ici, pas un contournement magique des règles des plateformes. Envoyer des messages non sollicités en masse à des particuliers reste une violation des CGU (comptes bannis) et, pour le démarchage téléphonique, une pratique encadrée par la loi — quel que soit l'outil utilisé pour l'automatiser. `automation/social_auto_poster.py` publie donc sur tes propres comptes (comme Buffer), et `automation/prospect_finder.py` *repère* automatiquement des partenaires locaux potentiels sans les contacter à ta place — l'envoi du message reste une décision humaine volontaire, avec le modèle prêt dans `marketing/supplier-outreach-message.md`.

Voir `SETUP_GUIDE.md` pour la suite.
