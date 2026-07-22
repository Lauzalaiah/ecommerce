# Guide de démarrage — de zéro à la première vente

Suis les étapes dans l'ordre. Chaque étape indique clairement ce qui est déjà prêt dans ce dépôt et ce qui reste à faire de ton côté (comptes, paiements — des actes que je ne peux pas poser à ta place).

## Étape 0 — Vendre cette semaine, sans attendre la boutique complète

Si l'objectif immédiat est de "faire tes premiers euros", commence par `fast-start/stripe-payment-link-quickstart.md`. Ça prend moins d'une heure et ça ne coûte rien tant qu'il n'y a pas de vente. Tu peux faire ça en parallèle des étapes suivantes.

Une page de liste d'attente est déjà en ligne et partageable dès maintenant : https://claude.ai/code/artifact/7718947d-bc93-4fa2-b690-83ed2b4f8ce8 — colle ce lien en bio Instagram/TikTok ou envoie-le à ton entourage pour commencer à capter des inscriptions avant même l'ouverture. Il te reste juste à brancher un formulaire Google Forms gratuit derrière (2-3 minutes, voir `fast-start/README-landing-page.md`) pour recevoir réellement les emails.

Aucune valeur à choisir toi-même pour les comptes à créer (Google Form, Shopify, Meta, Google Cloud, Stripe) : `fast-start/copy-paste-checklist.md` te donne tous les noms/réglages déjà décidés, prêts à coller.

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

Tu pars avec un avantage : un contact fournisseur déjà éprouvé. `marketing/supplier-outreach-message.md` contient un message prêt à envoyer (FR/EN) pour transformer cette relation ponctuelle en partenariat régulier, avec les bonnes questions à poser (catalogue, tarifs par palier, dropshipping ou gros, certificats). Utilise `marketing/partner-outreach-tracker.csv` pour suivre cet échange et les autres partenariats locaux du plan d'acquisition.

## Étape 5 — Paiements

Dans l'admin Shopify → **Paramètres → Paiements** : active Shopify Payments (ou Stripe/PayPal en alternative) pour encaisser par carte. Aucune donnée bancaire n'est à me transmettre, c'est une étape que tu dois faire toi-même dans l'admin.

## Étape 6 — Trouver tes premiers clients

C'est le cœur de `marketing/` :

- `marketing/launch-plan-30-60-90.md` — le plan d'action jour par jour, pensé pour zéro/petit budget au départ.
- `marketing/social-media-calendar.md` — 4 semaines de posts prêts à publier.
- `marketing/ad-copy-templates.md` — accroches publicitaires prêtes, à activer seulement une fois les premières ventes organiques obtenues.
- `marketing/email-flows.md` — séquences email (bienvenue, panier abandonné, post-achat, réactivation).
- `marketing/seo-guide.md` — trafic gratuit sur la durée.

## Sur les "agents IA" qui trouvent des clients

Des plateformes qui vendent des "agents IA marketing" (blink.new et d'autres) existent réellement — mais sous le capot, ces agents font de la recherche web, de la génération de contenu, ou de l'automatisation d'emails B2B : la même catégorie de choses que ce qui suit, pas un moyen de contourner les règles des plateformes. Envoyer des messages non sollicités en masse à des particuliers reste une violation des CGU (comptes bannis) et le démarchage téléphonique reste encadré par la loi, quel que soit l'outil utilisé pour l'automatiser.

Deux agents légitimes sont en place dans `automation/` :

- **Publication automatique** : 3 fois par semaine sur ta Page Facebook (et Instagram si tu ajoutes des photos), via l'API officielle Meta — le principe de Buffer, gratuit et sous ton contrôle total.
- **Recherche de prospects locaux** : sur simple déclenchement (tu indiques une ville), il interroge l'API Google Places et ajoute automatiquement les vétérinaires, toiletteurs, animaleries et éducateurs canins trouvés à `marketing/partner-outreach-tracker.csv`, prêts à être contactés avec le message de `marketing/supplier-outreach-message.md`.

Les deux nécessitent 10-15 minutes de configuration une fois (tes propres identifiants Meta/Google) — voir `automation/README.md`. Le contact reste volontaire et humain : c'est la limite légitime, pas une limite technique de ce dépôt.

## Ce qu'il reste uniquement à ta charge

- Créer les comptes (Shopify, Stripe, réseaux sociaux, app de dropshipping) — identité et moyens de paiement requis, je ne peux pas les créer à ta place.
- Générer tes jetons d'accès Meta pour l'automatisation réseaux sociaux (`automation/README.md`) et créer le Google Form de la liste d'attente (`fast-start/README-landing-page.md`) — ces deux étapes prennent quelques minutes chacune mais demandent tes propres comptes.
- Choisir et valider un fournisseur réel, y compris la vérification réglementaire pour l'alimentaire.
- Répondre aux messages et commandes clients au quotidien.
- Décider du budget publicitaire réel à engager, et quand.

## Prochaine mise à jour possible

Une fois que la boutique et le catalogue sont en ligne, dis-moi quels produits partent le mieux et quel canal (réseaux sociaux, recherche Google, bouche-à-oreille) amène le plus de visites — je peux affiner le thème, le catalogue ou le plan marketing en fonction de ces premiers résultats réels plutôt que d'hypothèses.
