# Séquences email prêtes à envoyer

Outil conseillé pour démarrer sans frais : **Shopify Email** (gratuit jusqu'à un certain volume, natif dans l'admin). Migration vers Klaviyo possible plus tard si le volume justifie des automatisations plus poussées.

## Séquence 1 — Bienvenue (déclenchée à l'inscription newsletter, voir section `newsletter.liquid`)

**Email 1 — immédiat**
> Objet : Votre code de bienvenue est là 🐾
> Corps : Merci de rejoindre [Nom boutique] ! Voici votre code **BIENVENUE10** pour -10% sur votre première commande. Chez nous, chaque produit est choisi pour le bien-être réel de votre chien ou chat — pas juste pour l'étiquette.
> CTA : Découvrir la boutique

**Email 2 — J+2**
> Objet : Comment on choisit nos produits
> Corps : Court texte sur les critères de sélection (ingrédients, absence d'additifs superflus, retours clients). Renforce la confiance avant l'achat.

**Email 3 — J+5**
> Objet : Ce que nos clients en disent
> Corps : 2-3 avis clients réels + rappel du code de bienvenue s'il n'a pas encore été utilisé.

## Séquence 2 — Panier abandonné

**Email 1 — 1h après abandon**
> Objet : Vous avez oublié quelque chose pour [nom de l'animal si connu / votre compagnon]
> Corps : Rappel des produits laissés dans le panier + réassurance (livraison rapide, satisfait ou remboursé).

**Email 2 — 24h après**
> Objet : Toujours intéressé ? Voici -5% pour finaliser
> Corps : Petite incitation ponctuelle, à utiliser avec parcimonie pour ne pas habituer les clients à attendre une réduction.

## Séquence 3 — Post-achat

**Email 1 — à l'expédition**
> Objet : Votre commande est en route !
> Corps : Numéro de suivi + estimation de livraison.

**Email 2 — J+10 après livraison estimée**
> Objet : Comment se passe la transition pour [nom de l'animal] ?
> Corps : Demande de retour honnête + lien direct vers formulaire d'avis. C'est la source principale des témoignages utilisés dans `testimonials.liquid`.

## Séquence 4 — Réactivation (clients inactifs depuis 60-90 jours)

> Objet : On ne vous a pas oublié — ni votre compagnon
> Corps : Rappel de l'offre d'abonnement récurrent (croquettes livrées automatiquement) + code de retour ponctuel si pertinent.

## Bonnes pratiques RGPD (obligatoires, pas optionnelles)

- N'envoyer ces emails qu'à des personnes ayant explicitement donné leur consentement (inscription newsletter ou achat).
- Toujours inclure un lien de désinscription visible (natif dans Shopify Email).
- Ne jamais acheter de liste d'emails externe — en plus d'être illégal en l'absence de consentement, cela détruit la délivrabilité de tous tes emails.
