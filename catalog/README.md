# Catalogue produits — `products_import.csv`

15 produits prêts à importer, couvrant les rayons classiques d'une animalerie physique : croquettes chien/chat (avec variantes de poids), friandises, compléments alimentaires, hygiène & soin, accessoires bien-être.

## Importer dans Shopify

1. Admin Shopify → **Produits** → **Importer** → sélectionne `products_import.csv`.
2. Coche "publier automatiquement sur tous les canaux de vente" si tu veux qu'ils soient visibles immédiatement.
3. Shopify regroupe automatiquement les lignes qui partagent le même `Handle` en un seul produit avec plusieurs variantes (ex. croquettes 2 kg / 12 kg).

## Ce qu'il te reste à faire avant de vendre

- **Photos** : la colonne `Image Src` est vide — j'ai laissé cette colonne volontairement vide plutôt que d'y mettre des URL inventées qui ne fonctionneraient pas. Deux sources réalistes :
  - Ton fournisseur (Alibaba/AliExpress ou autre) fournit presque toujours des photos produit HD utilisables — voir `../marketing/supplier-sourcing-alibaba-guide.md`.
  - Sinon, une photo prise au téléphone sur fond neutre suffit pour démarrer ; tu pourras les améliorer plus tard.
  - Une fois les photos prêtes, ajoute-les dans l'admin produit (glisser-déposer) ou remplis `Image Src` avec l'URL et ré-importe.
- **Prix** : les prix indiqués sont des repères de marché français, pas tes coûts réels. Ajuste-les selon ton prix d'achat fournisseur + marge visée (30 à 50 % de marge brute est courant sur ce secteur en dropshipping/retail).
- **Marque (`Vendor`)** : toutes les lignes utilisent "PattesZen" comme placeholder — remplace par ton vrai nom de marque avec un rechercher-remplacer avant import, ou modifie après coup dans l'admin.
- **Stock (`Variant Inventory Qty`)** : quantités d'exemple. Si tu pars en dropshipping (voir le guide fournisseurs), ce chiffre n'a plus vraiment de sens — désactive le suivi de stock (`Variant Inventory Tracker` → vide) pour ces produits-là.
- **Collections (étape indispensable, sinon les liens de la page d'accueil ne mènent nulle part)** : le thème (`shopify-theme/`) affiche des tuiles "Chiens / Chats / Compléments & santé / Hygiène & soin" et une section "Meilleures ventes" — elles ont besoin de vraies collections Shopify derrière. Admin Shopify → **Produits → Collections → Créer une collection**, en automatique avec ces conditions :
  - **Chiens** : condition `Tag` contient `chien`
  - **Chats** : condition `Tag` contient `chat`
  - **Compléments & santé** : condition `Type de produit` est égal à `Compléments alimentaires`
  - **Hygiène & soin** : condition `Type de produit` est égal à `Hygiène & soin`
  - **Meilleures ventes** : crée-la en collection **manuelle** au départ (pas de données de vente encore) et choisis toi-même 4-8 produits à mettre en avant ; tu la rendras automatique ("les plus vendus") une fois assez d'historique.

  Ensuite, dans **Personnaliser le thème** : colle le lien de chaque collection dans le réglage "Lien vers la collection" du bloc correspondant (section "Univers Chien/Chat/Bien-être"), et sélectionne la collection "Meilleures ventes" dans les réglages de la section du même nom.
