# Vendre cette semaine, avant même que la boutique Shopify soit prête

Le problème la dernière fois : payer Shopify chaque mois *avant* d'avoir des clients. Solution : encaisser tes premiers euros **avant** de remettre un abonnement complet en route, avec zéro code et (quasi) zéro frais fixe.

## Option A — Lien de paiement Stripe (le plus rapide, ~30 min)

1. Crée un compte sur stripe.com (gratuit, aucun abonnement — Stripe prend juste une commission par vente, environ 1,5 % + 0,25 € pour une carte européenne).
2. Dans le Dashboard Stripe → **Paiements** → **Liens de paiement** → **Créer un lien**.
3. Ajoute tes 3-5 produits phares (nom, photo, prix) issus de `catalog/products_import.csv`.
4. Stripe te donne un lien du type `buy.stripe.com/xxxx` pour chaque produit — mets-le en bio Instagram/TikTok, dans un post Facebook, ou envoie-le directement en message aux personnes intéressées.
5. Les paiements arrivent sur ton compte Stripe (virement automatique vers ta banque tous les quelques jours).

**Limites à connaître** : pas de panier multi-produits élégant, pas de gestion de stock automatique, tu dois traiter les commandes et l'expédition à la main (note commande + adresse dans un tableur). Très bien pour valider la demande avant d'investir dans la boutique complète.

## Option B — Shopify Starter (anciennement "Buy Button"), ~5 $/mois

Si tu veux rester 100 % dans l'écosystème Shopify (utile car `catalog/` et `shopify-theme/` sont prévus pour ça) :

1. Crée un compte Shopify → choisis le plan **Starter** (le moins cher, pensé pour vendre via réseaux sociaux/lien, sans site complet).
2. Importe `catalog/products_import.csv`.
3. Active le canal de vente "Réseaux sociaux" ou génère un **lien Shopify** par produit.
4. Poste ce lien avec les visuels — mêmes principes que l'option A.
5. Quand tu as tes premières ventes et un peu de trésorerie, tu montes de gamme vers le plan Basic pour débloquer le vrai site (celui préparé dans `shopify-theme/`).

## Ce que tu dois faire toi-même (je ne peux pas le faire à ta place)

- Créer les comptes (Stripe et/ou Shopify) — identité et moyen de paiement requis.
- Prendre ou récupérer des photos produit réelles (le CSV fourni n'en contient pas — voir `marketing/supplier-sourcing-alibaba-guide.md` pour en obtenir via un fournisseur).
- Répondre aux premiers messages clients — c'est aussi le meilleur moyen de comprendre ce qu'ils veulent vraiment avant de sur-investir.

Une fois 5 à 10 ventes passées via cette méthode, passe à `SETUP_GUIDE.md` pour la boutique complète — tu sauras déjà quels produits partent le mieux.
