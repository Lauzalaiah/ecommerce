# Thème Shopify — PattesZen (bien-être animal)

Ce dossier n'est **pas** un thème Shopify complet (recréer tout le moteur de panier, la recherche, les filtres, etc. depuis zéro n'a aucun intérêt : Shopify fournit déjà tout ça gratuitement et à jour). C'est un **pack de personnalisation** conçu pour être posé sur **Dawn**, le thème gratuit officiel de Shopify (Online Store 2.0), en 15-20 minutes.

## Installation

1. Dans l'admin Shopify → **Boutique en ligne** → **Thèmes** → **Explorer la bibliothèque de thèmes gratuits** → installe **Dawn**.
2. Via le Shopify CLI (`shopify theme dev` / `shopify theme push`) ou l'éditeur de code du thème dans l'admin, copie les fichiers de ce dossier dans la structure équivalente du thème Dawn :
   - `sections/*.liquid` → `sections/`
   - `snippets/*.liquid` → `snippets/`
   - `templates/*.json` → `templates/` (remplace ou fusionne avec l'existant, notamment `templates/index.json`)

Tous les textes de ces sections (titres, avis, FAQ, badges) sont éditables directement depuis **Personnaliser le thème**, sans toucher au code ni aux fichiers de traduction.
3. Dans l'éditeur de thème (Personnaliser), la page d'accueil doit maintenant proposer les sections : **Hero bien-être**, **Nos engagements**, **Univers Chien/Chat/Bien-être**, **Meilleures ventes**, **Abonnement croquettes**, **Avis clients**, **Réassurance**, **Newsletter**.
4. Remplace les textes/images placeholder par les tiens directement dans l'éditeur (aucun code à toucher).

## Pourquoi Dawn et pas un thème 100 % custom

Dawn est maintenu par Shopify, mis à jour en continu (accessibilité, vitesse, Core Web Vitals), et gratuit. Un thème 100 % fait main demande de réécrire le panier AJAX, la recherche prédictive, les filtres de collection, etc. — des semaines de travail pour réinventer ce que Dawn fait déjà bien. Les fichiers ici se concentrent sur ce qui différencie réellement ta boutique : la mise en avant du positionnement bien-être animal.

## Personnalisation rapide des couleurs/police

Dans **Personnaliser le thème → Paramètres du thème → Couleurs**, une palette suggérée pour un positionnement "bien-être" (apaisant, naturel, confiance) :
- Primaire : vert sauge `#5B7B63`
- Accent : terracotta doux `#D98B5F`
- Fond : blanc cassé `#FAF7F2`
- Texte : gris anthracite `#2E2A26`

## Fonctionnalités qui nécessitent une app (pas du thème)

- **Abonnement / livraison récurrente des croquettes** : la section `subscribe-save.liquid` ne fait que présenter l'offre ; la logique de facturation récurrente nécessite une app comme *Shopify Subscriptions* (gratuite) ou *Recharge*.
- **Programme de fidélité / parrainage** : app type *Smile.io*.
- **Avis clients vérifiés affichés automatiquement** : app type *Judge.me* ou *Loox* (la section `testimonials.liquid` fonctionne en attendant avec des avis saisis à la main).
