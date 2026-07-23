# Accélérer l'acquisition client — fondamentaux e-commerce (avatar, tracking, tests, upsells)

Ce qui suit couvre les leviers classiques qu'une formation e-commerce/dropshipping enseigne généralement une fois les bases posées (boutique, catalogue, premiers canaux) — cohérent avec `strategie-sans-contenu-video.md` et `proposition-de-valeur.md` déjà en place.

## 1. Avatar client précis — pour arrêter de parler à "tout le monde"

Un ciblage flou coûte cher en pub et affaiblit les messages. Avatar de départ pour PattesZen (à ajuster avec tes premières vraies données clients) :

> **Qui** : femme ou homme, 28-50 ans, propriétaire d'un chien ou chat depuis plus d'un an
> **Déclencheur d'achat** : son animal a un problème identifié (allergie, sensibilité digestive, articulations, anxiété) OU un vétérinaire/toiletteur lui a recommandé un changement
> **Frein principal** : a déjà une marque "par défaut" (supermarché) — a besoin d'une raison précise de changer, pas d'un joli produit de plus
> **Ce qui le convainc** : preuve que le produit résout SON problème précis (pas un argument générique bien-être), réassurance sur la livraison/le remboursement, avis d'autres propriétaires avec le même problème

Utilise cet avatar pour trancher : un mot-clé SEO, une accroche de pub ou un produit qui ne parle pas à cet avatar passe en second plan.

## 2. Tracking et retargeting — revendre à ceux qui ont déjà visité

Le levier le plus rentable une fois qu'il y a du trafic : relancer les visiteurs qui n'ont pas acheté du premier coup (la majorité, dans tous les e-commerce).

1. Admin Shopify → **Applications → Google & YouTube** et **Meta** (apps officielles gratuites) → connecte tes comptes Google Ads / Meta Business.
2. Ça installe automatiquement le Pixel Meta et le tag Google sur ta boutique (aucune ligne de code à toucher).
3. Une fois 100+ visiteurs cumulés, crée une audience de retargeting : "visiteurs des 30 derniers jours n'ayant pas acheté" et "paniers abandonnés" (Shopify envoie déjà un email automatique de relance panier abandonné nativement, en plus de celui prévu dans `email-flows.md`).
4. Budget de départ pour une campagne de retargeting : 3-5 €/jour — ce public a déjà montré de l'intérêt, le coût par vente y est presque toujours inférieur à une campagne d'acquisition froide.

## 3. Protocole de test publicitaire — au-delà des accroches déjà écrites

`ad-copy-templates.md` donne les textes ; voici la méthode pour les tester sans gaspiller le budget serré :

1. Lance au maximum 2 accroches en simultané, budget identique, minimum 4-5 jours sans y toucher (laisser l'algorithme apprendre).
2. Mesure une seule métrique de décision : coût par vente (pas le coût par clic, qui trompe souvent).
3. Coupe la moins bonne, garde la gagnante comme référence ("champion"), teste une nouvelle variante contre elle ("challenger") — jamais deux nouvelles variantes inconnues l'une contre l'autre.
4. N'augmente le budget d'une pub gagnante que par paliers de +20-30 %, jamais en le doublant d'un coup (l'algorithme "réapprend" et les performances peuvent chuter temporairement).

## 4. Vente additionnelle — augmenter la valeur par commande sans nouveau client

Moins cher que d'acquérir un client de plus : lui vendre plus au même moment.

- **Sur la fiche produit** : "Souvent acheté avec" — ex. croquettes + la friandise ou le complément assorti (app gratuite Shopify "Frequently Bought Together" ou équivalent, ou fait manuellement dans un premier temps en éditant les descriptions produit).
- **Au checkout / post-achat** : proposer un produit complémentaire à prix réduit juste après le paiement (apps type ReConvert, ou fonctionnalité native Shopify "Post-purchase upsell" selon le plan).
- Lien direct avec `proposition-de-valeur.md` point 1 : les packs que tu composes toi-même sont la version la plus aboutie de l'upsell — vendus comme solution complète, pas comme suggestion d'ajout.

## Comment tout ça s'articule avec ce qui existe déjà

Avatar (point 1) → resserre les mots-clés SEO (`seo-guide.md`), les accroches pub (`ad-copy-templates.md`), et les recherches de prospects locaux (`automation/prospect_finder.py`, en priorisant les vétérinaires spécialisés plutôt que génériques). Tracking (point 2) → se branche sur le trafic déjà généré par la page d'attente et le futur SEO. Upsells (point 4) → augmentent la rentabilité de chaque client acquis via n'importe lequel des canaux déjà en place, donc ça reste utile quel que soit le canal qui fonctionne le mieux pour toi.
