# Créer les comptes sans réfléchir — copie-colle

Tout ce qui suit a déjà été décidé pour toi (noms, catégories, réglages) : il ne te reste qu'à coller ces valeurs dans les formulaires de chaque plateforme et à valider la vérification (email/SMS/carte) que toi seul peux faire. Objectif : que chaque étape prenne 2-3 minutes de clics, zéro minute de réflexion.

## 1. Google Form (liste d'attente) — 2 min

- Titre : `Liste d'attente PattesZen`
- Champ 1 : `Prénom` — réponse courte, non obligatoire
- Champ 2 : `Email` — réponse courte, obligatoire, validation "Adresse e-mail"
- Une fois créé : Envoyer → onglet lien → copie l'URL et envoie-la-moi, je republie la page d'attente avec.
- **Pour vérifier que la page d'attente est bien publique** : ouvre le lien en navigation privée (donc déconnecté de ton compte) — si tu vois la page normalement, c'est bon. Je ne peux pas tester ça moi-même de façon fiable : mon accès passe par ton compte connecté, pas par une visite anonyme.

## 2. Shopify — 5 min

- Nom de la boutique : `PattesZen` (ou ton nom définitif si déjà choisi)
- Adresse `.myshopify.com` proposée : `pattes-zen` (Shopify en suggère une variante si déjà prise, accepte celle proposée)
- Secteur d'activité : `Animalerie` / `Pet Care`
- "Vendez-vous déjà ?" : Non / Je démarre
- Pays : France
- Plan : Starter (5 $/mois, vente via lien/réseaux) ou Basic (~29-36 €/mois, site complet) — voir `stripe-payment-link-quickstart.md` si tu hésites

## 3. App Meta (publication auto réseaux sociaux) — 5 min

- Sur developers.facebook.com → Créer une app
- Nom de l'app : `PattesZen Marketing`
- Type : `Entreprise`
- Permissions à cocher dans Graph API Explorer : `pages_manage_posts`, `pages_read_engagement`, `instagram_basic`, `instagram_content_publish`
- Détail complet : `../automation/README.md` section 1

## 4. Google Cloud (recherche de prospects locaux) — 3 min

- Nom du projet : `patteszen-prospection`
- API à activer : `Places API`
- Nom de la clé API : `patteszen-places-key`
- Restriction de la clé : "Places API" uniquement
- Détail complet : `../automation/README.md` section 2

## 5. Stripe (paiements / lien de paiement rapide) — 5 min

- Nom de l'entreprise : `PattesZen`
- Catégorie d'activité : `Pet Stores / Pet Supplies`
- Site web (si demandé avant que Shopify existe) : colle le lien de la page d'attente en attendant d'avoir l'URL définitive

## Après ça

Il n'y a rien d'autre à créer comme compte. Une fois ces 5 étapes faites, tout le reste (thème, catalogue, publication automatique, recherche de prospects, emails) tourne avec ce qui est déjà dans ce dépôt.
