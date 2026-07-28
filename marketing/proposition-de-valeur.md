# Ta proposition de valeur — au-delà du prix

Un maçon qui construit sa maison à la main vend une preuve matérielle (le bois, l'effort, le résultat visible). En dropshipping/revente, tu ne fabriques rien — donc ta valeur ne peut pas être "j'ai construit ce produit", mais elle peut être tout aussi réelle sur un autre plan : ce que ton implication personnelle *prouve* au client, là où une grosse boutique anonyme ne prouve rien. Les 5 angles ci-dessous sont honnêtes (rien à inventer, juste à documenter ce que tu fais déjà ou peux faire simplement), avec des textes prêts à coller.

## 1. La curation en packs — l'équivalent le plus direct du "construit à la main"

Assembler toi-même des produits en packs pour un problème précis, c'est un acte de construction réel : tu prends des matières premières (les produits fournisseur) et tu en fais quelque chose de plus utile que la somme des pièces.

> **Exemple de fiche produit — "Pack Anti-Allergies Chien"**
> Composé et testé par nous pour les chiens aux peaux sensibles : croquettes sans céréales au saumon + huile de saumon oméga-3 + shampoing hypoallergénique. Trois produits qu'on a choisi de faire fonctionner ensemble, pas juste mis côte à côte.

À faire quand tu es prêt : ajouter ces packs comme nouveaux produits dans `../catalog/products_import.csv` (un pack = un produit avec son propre prix, légèrement inférieur à la somme des 3 achetés séparément).

## 2. Le test personnel — la preuve de travail

> **Texte pour un bloc "Bénéfice produit" ou la page À propos**
> Chaque produit de cette boutique a été commandé et testé par nous avant d'être mis en vente — pas seulement listé depuis un catalogue fournisseur. Si un produit ne nous convainc pas, il n'apparaît pas ici.

Où le coller : dans l'admin Shopify → Personnaliser le thème → section "Bénéfices produit" (`shopify-theme/sections/product-benefits.liquid`), remplace un des blocs par défaut ("Sans céréales", etc.) par ce texte sur les produits concernés.

## 3. La spécialisation — l'expertise reconnue

Déjà engagé via `strategie-sans-contenu-video.md` : être *le* spécialiste d'un problème précis plutôt qu'une boutique généraliste. **Déjà appliqué par défaut** dans `shopify-theme/templates/index.json` et les réglages du Hero — le titre de la page d'accueil est maintenant "Une réponse précise au besoin de votre chien ou chat", plus le sous-titre nommant les problèmes concrets (allergies, digestion, articulations, anxiété). Tu peux l'ajuster dans l'éditeur de thème si tu veux reformuler, mais tu n'as plus à le faire depuis zéro.

## 4. La signature personnelle — l'histoire d'origine

> **Texte pour une page "À propos" (Boutique en ligne → Pages → Ajouter une page)**
> Cette boutique n'est pas tenue par une entreprise anonyme. Je m'appelle [ton prénom], et [nom de ton animal] a eu [problème précis rencontré] il y a quelques années — j'ai mis longtemps à trouver des produits qui fonctionnent vraiment, sans avoir à tout essayer au hasard. C'est pour ça que cette boutique existe : des produits que j'ai vérifiés moi-même, pour des problèmes que je connais.

Remplis les crochets avec ta vraie histoire — c'est ce qui rend ce texte crédible, pas la formulation. **Important** : le bouton secondaire du Hero pointe vers `/pages/a-propos` — quand tu crées la page, Shopify génère normalement cette même URL à partir du titre "À propos", mais vérifie-le (Boutique en ligne → Pages → ta page → l'URL affichée en bas) et corrige le réglage "Lien du bouton secondaire" du Hero si l'URL générée diffère.

## 5. Le service personnalisé — la présence après-vente

> **Texte pour la page Contact (`shopify-theme/templates/page.contact.json`) ou signature email**
> Une question sur quel produit choisir pour votre animal ? Écrivez-moi directement, je réponds personnellement — pas un service client générique.

Ce texte n'a de valeur que si tu réponds vraiment personnellement (au moins au début, avant tout volume) — c'est justement ce qui le différencie d'une grosse boutique.

## Par où commencer

Dans l'ordre du rapport effort/impact, vu ta situation (pas de vidéo, budget serré, boutique pas encore lancée) :

1. **Page À propos** (point 4) — 15 minutes, gratuit, zéro dépendance technique, un des textes qui convertit le mieux en confiance.
2. **Test personnel affiché** (point 2) — gratuit, juste une phrase honnête à condition de l'avoir vraiment fait (voir `supplier-sourcing-alibaba-guide.md` : commander un échantillon avant de lister).
3. **Titre spécialisé** (point 3) — 5 minutes dans l'éditeur de thème, déjà cohérent avec la stratégie sans contenu vidéo.
4. **Service personnalisé** (point 5) — gratuit, à activer dès le premier client.
5. **Packs** (point 1) — le plus structurant mais aussi le plus long à construire (choisir les combinaisons, tester, fixer les prix) — à faire une fois les premières ventes individuelles validées, pas avant.
