# Arrêter de dépendre de la bonne volonté — programme de parrainage traçable

Constat de départ, qui est juste et normal (pas une question de gens malhonnêtes) : personne n'investit du temps/mémoire à promouvoir quelque chose qui ne lui rapporte rien de concret, surtout face à ses propres priorités. "Je vais en parler" est une intention, pas un engagement — elle se dilue face au quotidien de la personne. Deux principes pour corriger ça, appliqués aux vétos/toiletteurs de `partner-outreach-tracker.csv` et à ton entourage :

## Principe 1 — Remplacer la promesse par un intérêt mesurable

Au lieu de demander "peux-tu recommander ma boutique", propose un code de réduction **nominatif et traçable** :

- Dans l'admin Shopify → **Réductions → Créer une réduction** → un code unique par partenaire, ex. `VETODUPONT10` (10% pour le client) et note en interne la commission que ça te déclenche à toi (ex. 5€ ou 10% reversés au vétérinaire par commande passée avec son code).
- Le partenaire n'a plus besoin de "se souvenir de dire du bien" — chaque fois qu'un client utilise son code, c'est vérifiable et il touche quelque chose. Son intérêt personnel devient aligné avec le tien, plutôt que de reposer sur sa mémoire ou sa gentillesse.
- Pour tes proches (pas de commission financière logique) : remplace par un système de parrainage classique ("10% pour toi, 10% pour ton ami" déjà mentionné dans `launch-plan-30-60-90.md`) — même logique, gain concret des deux côtés.

## Principe 2 — Rendre l'action passive, pas active

Ne compte pas sur le partenaire pour *dire* quelque chose à chaque client — donne-lui un support physique qui fait le travail à sa place, posé une fois pour toutes sur son comptoir :

> **Texte pour un flyer A6 à imprimer et déposer chez le partenaire**
> 🐾 [Nom du partenaire] recommande PattesZen
> Croquettes, compléments et soins pour le bien-être de votre chien ou chat, livrés chez vous.
> **-10% avec le code `[CODE-PARTENAIRE]`**
> [QR code pointant vers ta boutique, avec le code déjà pré-rempli si possible via un lien de réduction direct : `https://ta-boutique.myshopify.com/discount/[CODE-PARTENAIRE]`]

Un lien de réduction Shopify (format `/discount/CODE`) applique automatiquement le code au panier du client qui scanne — zéro action requise du partenaire après avoir posé le flyer une fois.

## Comment savoir qui tient vraiment sa promesse (et arrêter d'investir du temps sur ceux qui ne la tiennent pas)

- Admin Shopify → **Réductions** → chaque code affiche son nombre d'utilisations. Vérifie toutes les 2-3 semaines.
- Mets à jour `partner-outreach-tracker.csv` (colonne Notes) avec le nombre de ventes générées par partenaire.
- Ceux à zéro utilisation après plusieurs semaines : ce n'est pas la peine de continuer à solliciter, ni de leur en vouloir — ils n'ont simplement pas d'intérêt suffisant activé chez eux. Concentre ton temps sur ceux dont le code tourne réellement, et propose-leur d'aller plus loin (partenariat renforcé, plus grosse commission).

## Le principe général, au-delà des vétos

Ce mécanisme (intérêt mesurable + action passive + suivi de qui délivre vraiment) s'applique à n'importe quelle relation où tu comptais auparavant sur une promesse verbale — y compris avec ton entourage. Ce n'est pas cynique, c'est juste ne plus dépendre d'un facteur que tu ne contrôles pas (la mémoire/priorité de quelqu'un d'autre) quand un facteur que tu contrôles (l'incitation, le support physique) fait le même travail plus fiablement.
