# Guide de démarrage — de zéro à la première vente

Suis les étapes dans l'ordre. Chaque étape indique clairement ce qui est déjà prêt dans ce dépôt et ce qui reste à faire de ton côté (comptes, paiements — des actes que je ne peux pas poser à ta place).

## Étape 0 — Vendre cette semaine, sans attendre la boutique complète

Si l'objectif immédiat est de "faire tes premiers euros", commence par `fast-start/stripe-payment-link-quickstart.md`. Ça prend moins d'une heure et ça ne coûte rien tant qu'il n'y a pas de vente. Tu peux faire ça en parallèle des étapes suivantes.

## Étape 1 — Compte Shopify

1. Crée un compte sur shopify.com (ou réactive l'ancien si tu y as encore accès).
2. Choisis un plan : **Basic** (~29-36 €/mois selon la devise/promo en cours) pour un site complet, ou **Starter** (~5 $/mois) si tu veux d'abord vendre uniquement via lien/réseaux sociaux sans site complet (voir Étape 0, Option B).
3. Configure le nom de domaine (tu peux garder un sous-domaine `.myshopify.com` gratuit pour commencer, et acheter un vrai nom de domaine plus tard une fois les premières ventes faites).

## Étape 2 — Thème de la boutique

Suis `shopify-theme/README.md` : installer Dawn (gratuit) puis y déposer les fichiers de `shopify-theme/sections/`, `shopify-theme/snippets/` et `shopify-theme/templates/`. Résultat : une page d'accueil et une page produit orientées bien-être animal (hero, engagements, univers chien/chat, meilleures ventes, abonnement, avis, réassurance, newsletter, FAQ), toutes personnalisables sans code depuis l'éditeur de thème.

Pense à remplacer "PattesZen" par le nom de ta marque partout où il apparaît (titre du site, réglages du thème, catalogue).

## Étape 3 — Catalogue produits

Suis `catalog/README.md` : importer `catalog/products_import.csv` (15 produits couvrant croquettes, friandises, compléments, hygiène, accessoires). Ajuste ensuite les prix à tes coûts réels et ajoute de vraies photos (voir Étape 4 pour la source la plus simple).

## Étape 4 — Fournisseur / stock (le point qui a probablement bloqué la dernière fois)

Suis `marketing/supplier-sourcing-alibaba-guide.md`. Résumé : le dropshipping (via DSers ou CJ Dropshipping, connectés à des fournisseurs Alibaba/AliExpress) permet de vendre **sans acheter de stock à l'avance** — ça règle directement le problème "je payais la boutique avant d'avoir des clients". Attention particulière si tu vends des croquettes/friandises : ce sont des aliments soumis à réglementation à l'import, contrairement aux accessoires — le guide détaille ce point et par où commencer sans risque (accessoires d'abord, alimentaire une fois la démarche réglementaire vérifiée).

## Étape 5 — Paiements

Dans l'admin Shopify → **Paramètres → Paiements** : active Shopify Payments (ou Stripe/PayPal en alternative) pour encaisser par carte. Aucune donnée bancaire n'est à me transmettre, c'est une étape que tu dois faire toi-même dans l'admin.

## Étape 6 — Trouver tes premiers clients

C'est le cœur de `marketing/` :

- `marketing/launch-plan-30-60-90.md` — le plan d'action jour par jour, pensé pour zéro/petit budget au départ.
- `marketing/social-media-calendar.md` — 4 semaines de posts prêts à publier.
- `marketing/ad-copy-templates.md` — accroches publicitaires prêtes, à activer seulement une fois les premières ventes organiques obtenues.
- `marketing/email-flows.md` — séquences email (bienvenue, panier abandonné, post-achat, réactivation).
- `marketing/seo-guide.md` — trafic gratuit sur la durée.

## Sur les "agents" qui démarchent des clients

Ce point mérite d'être dit clairement plutôt que laissé dans le flou : il n'existe pas d'outil légitime (IA ou non) capable d'aller démarcher automatiquement de vrais clients humains à ta place sur les réseaux sociaux, par téléphone ou par message — les plateformes l'interdisent explicitement (spam, usurpation, RGPD pour les emails/téléphones), et ça se retourne généralement contre la boutique (comptes bannis, mauvaise réputation) plutôt que de générer de vraies ventes durables.

Ce que ce dépôt fournit à la place, et qui produit un effet réellement comparable en pratique : du contenu prêt à publier, des publicités prêtes à lancer, des emails automatisés une fois configurés (ils tournent ensuite sans intervention), et un plan d'action concret. C'est la version qui marche et qui ne met pas ta boutique en danger.

## Ce qu'il reste uniquement à ta charge

- Créer les comptes (Shopify, Stripe, réseaux sociaux, app de dropshipping) — identité et moyens de paiement requis, je ne peux pas les créer à ta place.
- Choisir et valider un fournisseur réel, y compris la vérification réglementaire pour l'alimentaire.
- Répondre aux messages et commandes clients au quotidien.
- Décider du budget publicitaire réel à engager, et quand.

## Prochaine mise à jour possible

Une fois que la boutique et le catalogue sont en ligne, dis-moi quels produits partent le mieux et quel canal (réseaux sociaux, recherche Google, bouche-à-oreille) amène le plus de visites — je peux affiner le thème, le catalogue ou le plan marketing en fonction de ces premiers résultats réels plutôt que d'hypothèses.
