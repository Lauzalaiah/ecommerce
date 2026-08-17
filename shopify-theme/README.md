# Thème Shopify — PattesZen (bien-être animal)

Ce dossier n'est **pas** un thème Shopify complet (recréer tout le moteur de panier, la recherche, les filtres, etc. depuis zéro n'a aucun intérêt : Shopify fournit déjà tout ça gratuitement et à jour). C'est un **pack de personnalisation** conçu pour être posé sur le thème gratuit officiel de Shopify — **Horizon** ou **Dawn** selon celui que Shopify te propose actuellement (les deux suivent la même architecture Online Store 2.0, les instructions ci-dessous marchent pour les deux).

## ⚠️ N'upload jamais ce dépôt (ni même ce dossier) comme fichier zip dans "Upload theme"

Ce n'est pas un thème autonome — il lui manque volontairement `layout/theme.liquid` et toute la structure de base (déjà fournie par Horizon/Dawn). Uploader un zip de ce dépôt donne l'erreur *"zip does not contain a valid theme: missing template layout/theme.liquid"*. La bonne méthode est un copier-coller dans l'éditeur de code du thème déjà installé, détaillée ci-dessous.

## Installation (copier-coller dans l'éditeur de code, pas d'upload de zip)

1. Le thème gratuit (Horizon ou Dawn) doit déjà être présent dans **Boutique en ligne → Thèmes** — sinon installe-le depuis la bibliothèque de thèmes gratuits de Shopify.
2. Sur ce thème → **⋯** → **Modifier le code**. Ajoute les fichiers **dans cet ordre précis** (les sections/templates référencent les snippets, donc les snippets d'abord) :
   1. **Snippets** → **Ajouter un nouveau snippet** → nomme-le exactement `icon-paw` (sans `.liquid`, Shopify l'ajoute automatiquement) → colle le contenu de `shopify-theme/snippets/icon-paw.liquid`. Répète pour `icon-benefit`.
   2. **Sections** → **Ajouter une nouvelle section** pour chacun de ces noms exacts, en collant le contenu du fichier `.liquid` correspondant : `hero-banner`, `value-props`, `featured-categories`, `subscribe-save`, `testimonials`, `trust-badges`, `newsletter`, `product-benefits`, `faq-accordion`, `announcement-bar`.
   3. **Templates** → ouvre `index.json` (déjà existant) → remplace tout son contenu par celui de `shopify-theme/templates/index.json`. Fais pareil pour `product.json`, et crée `page.contact.json` si tu veux la page contact prête à l'emploi (sinon le thème garde sa page contact par défaut).
3. Sauvegarde, puis **Personnaliser le thème** pour vérifier que la page d'accueil propose maintenant : **Barre d'annonce**, **Hero bien-être**, **Nos engagements**, **Univers Chien/Chat/Bien-être**, **Meilleures ventes**, **Abonnement croquettes**, **Avis clients**, **Réassurance**, **Newsletter**.
4. Remplace les textes/images placeholder par les tiens directement dans l'éditeur (aucun code à toucher pour cette partie).

Beaucoup de copier-coller : si tu as accès à un ordinateur, fais cette étape dessus plutôt que sur mobile, c'est nettement plus confortable. Ça reste faisable au téléphone, juste plus lent.

## Look plus premium — ce qui a changé

- **Icônes distinctes par bénéfice** : les sections "Nos engagements", "Réassurance", "Bénéfices produit" et "Barre d'annonce" ont chacune un sélecteur d'icône par bloc (livraison, garantie, naturel, bien-être, qualité, sécurité) au lieu de répéter la même icône patte partout — plus crédible visuellement.
- **Barre d'annonce** (nouvelle section, tout en haut de la page d'accueil) : bandeau fin avec tes réassurances principales (livraison, garantie, paiement sécurisé) — c'est la première chose vue par un visiteur.
- **Hero** : mini bandeau de réassurance sous les boutons, dégradé sur l'image pour que le texte reste lisible, légère animation d'apparition.
- **Cartes (avis, engagements)** : ombre et léger effet au survol, coins arrondis cohérents.
- **Urgence honnête sur la fiche produit** : la section "Bénéfices produit" peut afficher "Plus que X en stock" — activable dans ses réglages, basé sur le vrai stock Shopify (pas un chiffre inventé).

## Pourquoi Horizon/Dawn et pas un thème 100 % custom

Ces thèmes sont maintenus par Shopify, mis à jour en continu (accessibilité, vitesse, Core Web Vitals), et gratuits. Un thème 100 % fait main demande de réécrire le panier AJAX, la recherche prédictive, les filtres de collection, etc. — des semaines de travail pour réinventer ce qu'ils font déjà bien. Les fichiers ici se concentrent sur ce qui différencie réellement ta boutique : la mise en avant du positionnement bien-être animal.

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
