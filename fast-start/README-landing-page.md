# Page de liste d'attente — capter des clients avant même l'ouverture

Cette page (`landing-page.html`) est déjà en ligne, avec un lien partageable que tu peux coller dès aujourd'hui en bio Instagram/TikTok ou dans tes messages/groupes (voir `marketing/launch-plan-30-60-90.md`, Jours 1-7). Elle n'a besoin d'aucun compte Shopify pour exister.

**Important à comprendre** : cette page est hébergée sur claude.ai, en dehors de Shopify — elle n'a pas de base de données propre pour stocker les emails collectés. Il lui faut donc un formulaire externe gratuit pour recevoir réellement les inscriptions. C'est la seule étape encore à ta charge (2-3 minutes, nécessite un compte Google) :

## Brancher la collecte d'emails (une fois, 2-3 minutes)

1. Va sur forms.google.com (gratuit avec un compte Google) → **Nouveau formulaire**.
2. Ajoute 2 champs : "Prénom" (facultatif) et "Email" (obligatoire, validation "réponse courte" avec restriction email si possible).
3. En haut à droite → **Envoyer** → onglet lien 🔗 → copie l'URL (ressemble à `https://forms.gle/xxxxxxx`).
4. Ouvre `fast-start/landing-page.html`, tout en bas, remplace :
   ```
   var WAITLIST_FORM_URL = "https://forms.gle/REMPLACE_PAR_TON_LIEN";
   ```
   par ton vrai lien.
5. Dis-le-moi (ou redéploie toi-même si tu veux garder la main) : je republie la page en ligne avec le bon lien en une minute.

## Où voir les inscriptions

Dans Google Forms → onglet **Réponses** → l'icône verte (Sheets) exporte automatiquement chaque inscription dans une feuille de calcul en temps réel, avec horodatage. C'est ta première mini base de données clients, gratuite, sans rien à héberger.

## Pourquoi ne pas simplement stocker les emails directement dans la page

Une page publique sans compte ni serveur derrière elle ne peut pas retenir les informations que les visiteurs y saisissent — n'importe quelle page web "seule" a cette limite, ce n'est pas spécifique à cet outil. Passer par Google Forms (ou plus tard Klaviyo/Shopify une fois la boutique en ligne, voir `marketing/email-flows.md`) est la façon standard et gratuite de résoudre ça.

## Étape suivante une fois la boutique Shopify prête

Remplace à terme cette page d'attente par l'URL réelle de la boutique partout où tu l'as partagée, et importe la liste d'emails collectée dans **Shopify Email** ou ton outil d'emailing pour lancer la séquence de bienvenue (`marketing/email-flows.md`) avec le code `BIENVENUE10` déjà annoncé sur la page.
