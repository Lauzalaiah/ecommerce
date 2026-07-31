# Thème Shopify — PattesZen (bien-être animal)

Ce dossier n'est **pas** un thème Shopify complet (recréer tout le moteur de panier, la recherche, les filtres, etc. depuis zéro n'a aucun intérêt : Shopify fournit déjà tout ça gratuitement et à jour). C'est un **pack de personnalisation** conçu pour être posé sur **Dawn**, le thème gratuit officiel de Shopify (Online Store 2.0), en 15-20 minutes.

## Installation

1. Dans l'admin Shopify → **Boutique en ligne** → **Thèmes** → **Explorer la bibliothèque de thèmes gratuits** → installe **Dawn**.
2. Via le Shopify CLI (`shopify theme dev` / `shopify theme push`) ou l'éditeur de code du thème dans l'admin, copie les fichiers de ce dossier dans la structure équivalente du thème Dawn :
   - `sections/*.liquid` → `sections/`
   - `snippets/*.liquid` → `snippets/`
   - `templates/*.json` → `templates/` (remplace ou fusionne avec l'existant, notamment `templates/index.json`)

Tous les textes de ces sections (titres, avis, FAQ, badges) sont éditables directement depuis **Personnaliser le thème**, sans toucher au code ni aux fichiers de traduction.
3. Dans l'éditeur de thème (Personnaliser), la page d'accueil doit maintenant proposer les sections : **Barre d'annonce**, **Hero bien-être**, **Nos engagements**, **Univers Chien/Chat/Bien-être**, **Meilleures ventes**, **Abonnement croquettes**, **Avis clients**, **Réassurance**, **Newsletter**.
4. Remplace les textes/images placeholder par les tiens directement dans l'éditeur (aucun code à toucher).

## Look plus premium — ce qui a changé

- **Icônes distinctes par bénéfice** : les sections "Nos engagements", "Réassurance", "Bénéfices produit" et "Barre d'annonce" ont chacune un sélecteur d'icône par bloc (livraison, garantie, naturel, bien-être, qualité, sécurité) au lieu de répéter la même icône patte partout — plus crédible visuellement.
- **Barre d'annonce** (nouvelle section, tout en haut de la page d'accueil) : bandeau fin avec tes réassurances principales (livraison, garantie, paiement sécurisé) — c'est la première chose vue par un visiteur.
- **Hero** : mini bandeau de réassurance sous les boutons, dégradé sur l'image pour que le texte reste lisible, légère animation d'apparition.
- **Cartes (avis, engagements)** : ombre et léger effet au survol, coins arrondis cohérents.
- **Urgence honnête sur la fiche produit** : la section "Bénéfices produit" peut afficher "Plus que X en stock" — activable dans ses réglages, basé sur le vrai stock Shopify (pas un chiffre inventé).

## Pourquoi Dawn et pas un thème 100 % custom

Dawn est maintenu par Shopify, mis à jour en continu (accessibilité, vitesse, Core Web Vitals), et gratuit. Un thème 100 % fait main demande de réécrire le panier AJAX, la recherche prédictive, les filtres de collection, etc. — des semaines de travail pour réinventer ce que Dawn fait déjà bien. Les fichiers ici se concentrent sur ce qui différencie réellement ta boutique : la mise en avant du positionnement bien-être animal.

## Personnalisation rapide des couleurs/police

Dans **Personnaliser le thème → Paramètres du thème → Couleurs**, la palette utilisée par défaut dans le hero (déjà cohérente avec `fast-start/landing-page.html`) :
- Primaire : vert sauge `#5B7B63`
- Accent : brique/terracotta `#A85C3F`
- Fond : porcelaine `#EEF1EC`
- Texte : pin profond `#1B2A22`
- Doré (petites touches, badges) : `#C79A44`

## Attention avant de publier les textes (risque légal réel)

En Personnalisant le thème, ne laisse aucun texte affirmer quelque chose que tu ne peux pas prouver — ex. "Recommandé par des vétérinaires", "certifié", "n°1 des ventes" — sans preuve réelle derrière (un vrai partenariat vétérinaire, une vraie certification). En France, une allégation commerciale trompeuse relève de l'**article L.132-2 du Code de la consommation** : jusqu'à 2 ans d'emprisonnement et une amende pouvant atteindre 10 % du chiffre d'affaires. Ce n'est pas théorique — voir `../marketing/obligations-legales-fiscales.md`. Le bloc "Recommandé par des vétérinaires" que la section Bénéfices produit contenait par défaut a été remplacé par un texte que tu peux honnêtement affirmer ("Vérifié avant mise en vente") ; ne le remets que si tu as un vrai partenariat vétérinaire à citer.

Même vigilance sur la section **Avis clients** : les faux avis sont explicitement listés comme pratique commerciale trompeuse (au même titre que les fausses allégations). Le bloc par défaut a été changé pour un texte d'exemple clairement instructif ("Remplace ce texte par un vrai avis reçu d'un vrai client") plutôt qu'un faux avis à l'apparence réaliste — remplace-le uniquement par de vrais avis reçus, jamais inventés, même au début quand tu n'en as encore aucun.

De même pour la **Barre d'annonce** ("Livraison offerte dès 39€", etc.) : n'affiche que des conditions que tu appliques réellement.

**Point de vigilance spécifique** : plusieurs textes par défaut promettent "Livraison 24-48h" et "Expédié depuis la France" (hero, engagements, bénéfices produit, réassurance). Ces textes sont **vrais uniquement** si tu stockes/expédies toi-même depuis la France ou via un entrepôt européen. Si tu choisis le dropshipping direct depuis l'Asie (Option A dans `../marketing/supplier-sourcing-alibaba-guide.md`, délais réels de 1 à 3 semaines), ces deux affirmations deviennent fausses et retombent sous le même risque L.132-2 que les avis inventés — remplace-les par une formulation honnête (ex. "Expédition sous 5-15 jours ouvrés") avant de publier. C'est le seul vrai point de friction entre le catalogue/thème et le choix de fournisseur : à trancher avant le lancement, pas après.

## Fonctionnalités qui nécessitent une app (pas du thème)

- **Abonnement / livraison récurrente des croquettes** : la section `subscribe-save.liquid` ne fait que présenter l'offre ; la logique de facturation récurrente nécessite une app comme *Shopify Subscriptions* (gratuite) ou *Recharge*.
- **Programme de fidélité / parrainage** : app type *Smile.io*.
- **Avis clients vérifiés affichés automatiquement** : app type *Judge.me* ou *Loox* (la section `testimonials.liquid` fonctionne en attendant avec des avis saisis à la main).
