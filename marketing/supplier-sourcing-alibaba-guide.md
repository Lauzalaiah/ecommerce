# Alibaba et sourcing fournisseur — ce qui est réellement possible

## D'abord, clarifier un point important

Il n'existe pas de "canal de vente Alibaba" pour Shopify — on ne peut pas "incorporer sa boutique à Alibaba" comme on le ferait avec Instagram ou Google. **Alibaba.com est une place de marché B2B** : elle sert à trouver des fournisseurs/fabricants (souvent en Chine) qui vendent en gros, pas à toucher des clients finaux. Le lien avec ta boutique se fait dans l'autre sens : tu utilises Alibaba (ou AliExpress, sa version davantage tournée vers la vente à l'unité) **pour t'approvisionner**, puis tu vends toi-même à tes clients via ta boutique Shopify.

C'est une bonne nouvelle pour ton problème de trésorerie : bien utilisé, ça permet de démarrer **sans gros investissement initial en stock**.

## Deux façons de travailler avec un fournisseur trouvé sur Alibaba

### Option A — Dropshipping (le plus adapté à ta situation actuelle)

Tu ne stockes rien : le fournisseur expédie directement au client final quand une commande arrive sur ta boutique.

1. Installe une app Shopify de dropshipping : **DSers** (spécialisée AliExpress, gratuite pour démarrer) ou **CJ Dropshipping** (catalogue plus large, inclut parfois du contrôle qualité).
2. Recherche les mêmes produits que ceux de `catalog/products_import.csv` chez des fournisseurs notés (4,7★ et plus, avec un historique de commandes conséquent).
3. Quand un client commande sur ta boutique, l'app transmet automatiquement la commande au fournisseur, qui expédie directement — tu encaisses la différence entre ton prix de vente et le prix fournisseur.
4. Commande d'abord un échantillon toi-même pour vérifier la qualité réelle avant de le proposer à tes clients.

**Avantage direct pour ton problème initial** : zéro argent immobilisé en stock, donc zéro risque de te retrouver à payer une boutique pleine de produits invendus.
**Inconvénient à connaître** : délais de livraison souvent plus longs (1-3 semaines depuis l'Asie, sauf entrepôts européens sur CJ Dropshipping) — à annoncer clairement sur ta boutique pour ne pas décevoir.

### Option B — Achat en gros, tu gères le stock et l'envoi

Tu commandes une quantité plus importante directement via Alibaba.com (souvent en passant par la fonction "Trade Assurance"), tu reçois la marchandise, tu stockes et expédies toi-même (ou via un prestataire logistique).

- Marge généralement meilleure, plus de contrôle sur la qualité et les délais.
- Nécessite un peu de trésorerie de départ et un espace de stockage.
- À envisager une fois que le plan `launch-plan-30-60-90.md` a confirmé une vraie demande sur un produit précis — pas avant.

## Point d'attention réglementaire — spécifique à l'alimentation animale

Contrairement à un accessoire (jouet, brosse, panier), **les croquettes et friandises sont des aliments pour animaux**, soumis en France/UE à une réglementation spécifique (notamment le règlement européen sur l'hygiène des aliments pour animaux et l'enregistrement de l'activité auprès des autorités compétentes, en France la DDPP/DGCCRF). Importer de la nourriture animale depuis l'Asie implique des démarches d'étiquetage, de déclaration et parfois de contrôle sanitaire aux frontières. Ce n'est pas un obstacle insurmontable — beaucoup de petites marques françaises le font — mais ce n'est pas à improviser : avant de te lancer sur les croquettes/friandises en particulier, vérifie ce point auprès de la DGCCRF ou d'un professionnel (expert-comptable spécialisé import, ou avocat spécialisé), surtout si tu passes en achat en gros (option B). En dropshipping (option A) avec un partenaire déjà organisé pour l'envoi en France, une partie de cette charge est en général déjà gérée par le fournisseur — vérifie-le explicitement avec lui avant de lister le produit.

Pour les produits non alimentaires (jouets, paniers, brosses, litière, lingettes, diffuseurs), il n'y a pas de contrainte spécifique au-delà du marquage CE standard des produits de consommation.

## Sécurité avec un nouveau fournisseur (bonnes pratiques standards, pas une accusation)

Tu mentionnes avoir déjà eu de bons retours avec une vendeuse — c'est une base solide pour continuer avec elle. Ces règles s'appliquent à *tout* fournisseur, connu ou nouveau, et sont les pratiques standards recommandées par Alibaba lui-même :

- Toujours payer via le système **Trade Assurance** d'Alibaba (protection en cas de non-conformité ou non-livraison) plutôt que par virement bancaire direct hors plateforme, même si le fournisseur le demande "pour aller plus vite".
- Commander un échantillon avant toute commande en gros.
- Demander les certificats pertinents (conformité, origine, sanitaire pour l'alimentaire) et vérifier qu'ils correspondent à une entreprise réellement enregistrée.
- Se méfier d'une pression à payer vite, en dehors de la plateforme, ou d'un prix anormalement bas par rapport au marché — signaux classiques à vérifier avant d'engager une somme importante.

## Par où commencer concrètement

1. Cette semaine : installer DSers ou CJ Dropshipping, chercher 2-3 fournisseurs pour les produits accessoires (jouets, paniers, brosses — pas de contrainte réglementaire) et commander un échantillon.
2. Une fois validé et une vraie demande confirmée par le plan d'acquisition, envisager les croquettes/friandises en vérifiant au préalable le point réglementaire ci-dessus.
3. Utiliser les vraies photos fournies par le fournisseur pour compléter `catalog/products_import.csv` (colonne `Image Src`).
