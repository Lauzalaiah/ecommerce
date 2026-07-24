# Automatisation marketing — deux agents légitimes

Ce dossier contient deux automatisations distinctes, chacune couvrant une partie de "trouver des clients" sans franchir la ligne entre marketing automatisé (légal, courant — c'est aussi ce que font en coulisses des outils qui se présentent comme des "agents IA marketing") et démarchage individuel non sollicité (interdit par les CGU des réseaux sociaux et encadré par la loi pour le téléphone/l'emailing grand public, quel que soit l'outil utilisé pour l'automatiser) :

1. **`social_auto_poster.py`** — publie automatiquement, 3 fois par semaine, le prochain post de `content_calendar.json` sur ta Page Facebook (et Instagram si une photo est renseignée). Même principe que Buffer ou Meta Business Suite : ça publie sur tes propres comptes publics, ça ne contacte personne individuellement.
2. **`prospect_finder.py`** — repère automatiquement des partenaires locaux potentiels (vétérinaires, toiletteurs, animaleries, éducateurs canins) via l'API Google Places, et les ajoute à `../marketing/partner-outreach-tracker.csv`. C'est un agent de *recherche* de prospects, pas de *contact* : il te donne la liste, l'envoi du message (voir `../marketing/supplier-outreach-message.md`) reste une action volontaire de ta part — comme un commercial qui prépare son fichier de prospection avant d'appeler.

---

## 1. Publication automatique réseaux sociaux

### Mise en place (une fois, 10-15 minutes)

1. **Convertir ton compte Instagram en compte professionnel** (Paramètres → Compte → Passer à un compte professionnel) et le lier à ta Page Facebook.
2. Sur [developers.facebook.com](https://developers.facebook.com) → **Mes apps** → **Créer une app** → type "Entreprise".
3. Va sur [developers.facebook.com/tools/explorer](https://developers.facebook.com/tools/explorer) (Graph API Explorer) :
   - En haut, sélectionne ton app dans le menu déroulant, puis ta Page dans "User or Page" (pas ton profil personnel).
   - Bouton **Add Permissions** → coche `pages_manage_posts`, `pages_read_engagement`, `instagram_basic`, `instagram_content_publish`.
   - **Generate Access Token** → autorise dans la fenêtre Facebook qui s'ouvre.
4. Ce token dure 1h — échange-le contre un **token longue durée** (~60 jours) : copie-le, va sur [developers.facebook.com/tools/debug/accesstoken](https://developers.facebook.com/tools/debug/accesstoken/), colle-le, **Debug**, puis en bas de la page **Extend Access Token**. Ce nouveau token devient `FB_PAGE_ACCESS_TOKEN`. Renouvelle-le à l'approche de l'expiration.
5. Récupère ton `FB_PAGE_ID` : dans Graph API Explorer, tape `me?fields=id,name` dans la barre de requête → **Submit** — le nombre affiché est ton `FB_PAGE_ID` (aussi visible dans **Paramètres de la Page → Informations sur la Page**).
6. Récupère ton `IG_BUSINESS_ACCOUNT_ID` (optionnel, pour publier aussi sur Instagram) : dans Graph API Explorer, tape `{FB_PAGE_ID}?fields=instagram_business_account` (remplace `{FB_PAGE_ID}` par le vrai numéro de l'étape 5) → **Submit** — le nombre dans `instagram_business_account.id` est ton `IG_BUSINESS_ACCOUNT_ID`.

### Secrets GitHub à ajouter

Dépôt GitHub → **Settings → Secrets and variables → Actions → New repository secret** :
- `FB_PAGE_ID`
- `FB_PAGE_ACCESS_TOKEN`
- `IG_BUSINESS_ACCOUNT_ID` (optionnel, seulement pour publier aussi sur Instagram)

### Tester avant de laisser tourner seul

Onglet **Actions** → workflow "Publication automatique réseaux sociaux" → **Run workflow** → vérifie sur ta Page que le post est bien apparu.

### Limite à connaître

Instagram exige une photo pour publier — tant que `image_url` est vide dans `content_calendar.json`, seul Facebook reçoit le post (le script le signale dans les logs). Ajoute l'URL dès que tu as de vraies photos produit.

### Ajuster le rythme ou le contenu

- Posts : édite `content_calendar.json`.
- Fréquence : modifie le `cron` dans `.github/workflows/social-auto-post.yml` et `POST_INTERVAL_DAYS` dans `social_auto_poster.py` en conséquence.

---

## 2. Recherche automatique de prospects locaux

### Mise en place (une fois, 5 minutes)

1. Sur [console.cloud.google.com](https://console.cloud.google.com), crée un projet (ou réutilise un existant), active l'API **Places API**, et génère une clé API (**API et services → Identifiants → Créer des identifiants → Clé API**).
2. Restreins cette clé à l'API Places uniquement (option proposée à la création) — bonne pratique de sécurité.
3. Un compte Google Cloud avec facturation activée est requis, mais Google offre ~200 $/mois de crédit gratuit récurrent : pour un usage ponctuel (quelques villes, une poignée de catégories), tu resteras sous ce seuil et ne paieras rien. Vérifie tes quotas/factures dans la console si tu prospectes beaucoup de villes.
4. Ajoute le secret `GOOGLE_PLACES_API_KEY` dans **Settings → Secrets and variables → Actions**.

### Lancer une recherche

Onglet **Actions** → workflow "Recherche de prospects locaux" → **Run workflow** → renseigne la ville (ex. "Lyon, France") → **Run workflow**. Les nouveaux prospects trouvés (nom, téléphone/site web, statut "A contacter") sont ajoutés et commités automatiquement dans `marketing/partner-outreach-tracker.csv` — sans doublon si tu relances plus tard pour une autre ville.

### Et ensuite

Le contact reste manuel et volontaire : ouvre le tracker, reprends la trame de `../marketing/supplier-outreach-message.md` (adaptée à un partenariat local plutôt qu'à un fournisseur) et personnalise-la pour chaque prospect. C'est la limite légitime — un agent qui enverrait ces messages sans validation humaine franchirait la ligne du démarchage non sollicité, quelle que soit la plateforme utilisée pour le construire.
