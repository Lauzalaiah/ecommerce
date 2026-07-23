# Créer les comptes sans réfléchir — copie-colle

Tout ce qui suit a déjà été décidé pour toi (noms, catégories, réglages) : il ne te reste qu'à coller ces valeurs dans les formulaires de chaque plateforme et à valider la vérification (email/SMS/carte) que toi seul peux faire. Objectif : que chaque étape prenne 2-3 minutes de clics, zéro minute de réflexion.

## 0. Statut auto-entrepreneur — ~20-30 min + délai d'obtention du SIRET (à faire en premier, avant toute vente)

Contrairement aux comptes ci-dessous, celui-ci n'est pas optionnel ni juste pratique : vendre sans immatriculation n'est pas légal en France, même via le lien Stripe rapide (voir `../marketing/obligations-legales-fiscales.md`). C'est donc la vraie étape 0.

- Site officiel et gratuit : **formalites.entreprises.gouv.fr** (guichet unique) — ou **autoentrepreneur.urssaf.fr**, qui redirige vers le même guichet.
- Parcours : "Créer une entreprise" → personne physique → micro-entreprise / auto-entrepreneur.
- Activité à déclarer : `Vente à distance de produits de bien-être animal (alimentation, accessoires) via internet` — code NAF généralement attribué automatiquement pour ce type d'activité : `47.91B` (Vente à distance sur catalogue spécialisé) — c'est l'administration qui l'attribue, pas à choisir toi-même.
- Adresse de l'entreprise : ton domicile (autorisé pour une activité en ligne, pas besoin de local commercial).
- Date de début d'activité : le jour où tu veux pouvoir commencer à vendre légalement.
- Régime social : micro-social simplifié (coché par défaut).
- Case "versement libératoire de l'impôt sur le revenu" : à cocher seulement si ton revenu fiscal de référence est sous le seuil en vigueur (vérifie ton dernier avis d'imposition) — sinon laisse décochée.
- Vérifie la case **ACRE** (réduction des cotisations sociales la 1ère année, sous conditions — demandeur d'emploi, moins de 26 ans, etc.) — proposée pendant l'inscription, gratuite à demander si éligible.
- À préparer avant de commencer : pièce d'identité (CNI ou passeport), justificatif de domicile de moins de 3 mois.

**Après l'inscription :**
- Le numéro **SIRET** arrive sous quelques jours à quelques semaines (email/courrier) — tu ne peux légalement facturer qu'une fois obtenu.
- Crée ensuite ton compte sur `autoentrepreneur.urssaf.fr` pour déclarer ton chiffre d'affaires (mensuel ou trimestriel, à choisir) — **déclaration obligatoire même à 0 €**, sinon pénalité.
- Ouvre un compte bancaire séparé pour l'activité dès que possible (obligatoire légalement seulement au-delà de 10 000 € de CA sur 2 années consécutives, mais plus simple à gérer dès le départ).

Coût : l'inscription est gratuite. Les cotisations sociales (environ 12,3 % du CA pour la vente de marchandises, taux à vérifier au moment de l'inscription car réévalué périodiquement) ne se paient que sur ce que tu déclares avoir réellement vendu — zéro vente = zéro cotisation. À partir de la 2ᵉ année, une taxe locale (CFE) s'ajoute généralement — pas d'action à prendre maintenant, juste à anticiper.

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

Il n'y a rien d'autre à créer comme compte. Une fois ces 6 étapes faites (le statut auto-entrepreneur en premier), tout le reste (thème, catalogue, publication automatique, recherche de prospects, emails) tourne avec ce qui est déjà dans ce dépôt.
