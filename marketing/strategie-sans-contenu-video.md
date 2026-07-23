# Stratégie d'acquisition sans création de contenu vidéo

`launch-plan-30-60-90.md` misait beaucoup sur les réseaux sociaux organiques (Instagram/TikTok) — aujourd'hui, la portée organique y dépend fortement de la vidéo (Reels/TikTok), que tu ne veux pas produire. Ce document reprend la priorité des canaux en partant de cette contrainte, et recentre le positionnement sur les moments où un client a un **besoin précis à résoudre**, plutôt qu'une envie à faire naître — le même principe qui fait qu'on va au supermarché sans pub, parce qu'on a faim.

## Le principe de base : 3 leviers, il faut en actionner au moins un

Zéro contenu + zéro budget + zéro effort de mise en relation ne fonctionne nulle part, avec ou sans vidéo — être inconnu au lancement est universel, y compris pour les boutiques qui font beaucoup de contenu (un créateur part aussi de zéro abonné). Il y a trois leviers pour en sortir, et la vidéo n'est qu'un choix possible parmi trois :

1. **Le temps** — SEO, prospection vétos/toiletteurs, réponses utiles dans des groupes spécialisés. Gratuit, lent (semaines/mois).
2. **L'argent** — Google Shopping/Search Ads. Rapide (jours), mais ça coûte, même un petit budget.
3. **Le contenu** — réseaux sociaux, vidéo ou texte. Gratuit, mais demande de la régularité et un délai avant résultats.

Ce document mise sur les leviers 1 et 2, puisque le levier 3 (vidéo) est exclu par contrainte personnelle.

## Deux familles de besoins, deux canaux différents

- **Besoin aigu** ("mon chien a des allergies", "j'ai faim") → la personne cherche déjà activement. Elle se trouve via une recherche, une recommandation, une plateforme d'achat. Pas besoin de créer l'envie, juste d'être présent au bon moment.
- **Envie/découverte** (un bel accessoire, un produit "sympa") → il faut créer le désir. C'est le terrain du contenu et de la vidéo — celui qu'on évite ici.

Le bien-être animal a de vrais moments de besoin aigu : allergies, troubles digestifs, calculs urinaires, arrivée d'un chiot/chaton, recommandation du vétérinaire, animal senior. Le catalogue (`../catalog/products_import.csv`) couvre déjà plusieurs de ces cas (sans céréales, glucosamine senior, anti-stress) — le changement à faire est de mettre ce positionnement "solution à un problème" en avant, plutôt qu'un discours générique "bien-être/lifestyle".

## Priorité des canaux (aucun ne nécessite de vidéo)

### 1. Google Shopping / Search Ads — capte une intention déjà là

- Dans l'admin Shopify → **Applications → Google & YouTube** (app gratuite officielle) → connecte un compte Google Merchant Center → synchronise le catalogue.
- Lance une campagne **Shopping** ciblée sur des recherches précises : "croquettes chien allergie", "croquettes chat calculs urinaires", "complément articulations chien senior avis".
- Budget de test : 5-10 €/jour. Contrairement à une pub Instagram qui interrompt quelqu'un, une pub Search répond à une recherche déjà faite — taux de conversion généralement bien supérieur pour un budget équivalent.

### 2. Réseau vétérinaires/toiletteurs — le vrai "moment du besoin"

Déjà en place : `../automation/prospect_finder.py` (trouve les vétos/toiletteurs/animaleries du coin) + `../marketing/supplier-outreach-message.md` (à adapter pour un partenariat local plutôt qu'un fournisseur). C'est le canal le plus proche de ton exemple du supermarché : le vétérinaire identifie le besoin, toi tu es la solution proposée.

### 3. SEO écrit ciblé sur des symptômes/problèmes précis

Complète `seo-guide.md` avec des recherches encore plus précises que les mots-clés déjà listés :
- "que donner à un chien qui a la diarrhée"
- "meilleure croquette chat calculs urinaires"
- "chiot qui ne mange pas que faire"
- "chien senior perd du poids alimentation"

Chaque article répond à un problème concret, pas à une envie — aucune vidéo requise, juste du texte utile qui se positionne sur Google au fil des mois.

### 4. Marketplaces (Amazon, Cdiscount)

Les acheteurs y cherchent déjà avec intention d'achat. Lister quelques produits phares là-bas (via l'app Shopify "Amazon" ou manuellement) t'apporte des clients sans avoir à construire une audience.

### 5. Groupes/forums spécialisés par problème, pas par contenu

Rejoins des groupes type "chien allergique", "chat insuffisance rénale" (pas les groupes génériques "chiens [ville]" du plan initial) et réponds utilement quand quelqu'un demande une recommandation — c'est le moment exact où ton produit résout un problème réel, sans avoir rien publié toi-même.

## 6. TikTok organique + payant — en externalisant la vidéo plutôt qu'en la filmant toi-même

Beaucoup de formations dropshipping (dont celle que tu suis) misent sur le tandem TikTok organique + TikTok Ads, construit autour de créatives vidéo. Ce n'est pas incompatible avec "pas de vidéo de ta part" : la production peut être externalisée (freelances UGC type Fiverr, agences spécialisées) plutôt que filmée par toi.

Si tu veux rouvrir ce canal sans apparaître à l'écran, une fois 2-3 produits validés via les canaux sans vidéo ci-dessus :

1. Commande un échantillon et envoie-le à 1-2 créateurs UGC (recherche "UGC pet creator" ou "UGC créateur animaux" sur Fiverr, ou dans des groupes de créateurs francophones) pour qu'ils filment une vidéo "test/unboxing" avec leur propre animal — compte quelques dizaines d'euros par vidéo.
2. Utilise cette vidéo en publicité TikTok Ads plutôt qu'en organique (même principe de compte pro que Meta, voir `../automation/README.md`) — un petit budget de test suffit pour commencer.
3. Des outils comme Minea (recherche de produits/créatives gagnantes) ou Triplewhale (analytics pub) reviennent souvent dans ces formations — ce sont des abonnements payants, pas indispensables tant que le budget est serré : les statistiques natives Shopify et TikTok Ads suffisent pour démarrer.

## Ce qui reste en place, mais en second plan

`automation/social_auto_poster.py` continue de tourner (c'est gratuit et automatique) — mais ne compte pas dessus comme moteur principal d'acquisition tant qu'il ne publie que du texte. Si un jour tu changes d'avis sur la vidéo (même une simple vidéo du produit ou de l'animal, sans toi à l'écran), ça redevient pertinent — mais ce n'est plus une condition pour vendre.

## Conclusion sur "garder ou non le bien-être animal"

Garder le secteur, changer l'angle : le problème n'était pas le marché mais le canal (contenu/désir au lieu de recherche/besoin). Les vrais atouts déjà acquis — la relation fournisseur, le catalogue, le thème — restent valables ; il s'agit de vendre "une solution à un problème animal précis", trouvable au moment où le problème se pose, plutôt que "un joli produit bien-être" qu'il faudrait faire désirer.
