# Obligations légales et fiscales — checklist boutique e-commerce en France

Ce point n'avait pas été couvert jusqu'ici. Ce qui suit est une checklist générale, pas un avis juridique — les seuils et règles évoluent et dépendent de ta situation exacte : fais valider ton statut avant ton premier euro de chiffre d'affaires par un expert-comptable (une première consultation est souvent gratuite ou à faible coût, y compris via des plateformes en ligne pour auto-entrepreneurs).

## 1. Statut juridique — avant de vendre quoi que ce soit

- Pour démarrer seul avec un volume incertain : le statut **auto-entrepreneur / micro-entreprise** est le plus simple (déclaration en ligne via le guichet unique de l'INPI, obtention d'un numéro SIRET).
- Vendre sans immatriculation, même en test, n'est pas légal en France — y compris les premières ventes via le lien Stripe de `fast-start/`.
- Le régime micro-entreprise a un plafond de chiffre d'affaires annuel (vente de marchandises) et un taux de cotisations sociales forfaitaire sur ce CA — vérifie les montants à jour sur **autoentrepreneur.urssaf.fr**, ils sont réévalués chaque année.

## 2. TVA

- En dessous d'un certain seuil de chiffre d'affaires, tu es en **franchise en base de TVA** : tu ne factures pas de TVA, avec la mention obligatoire "TVA non applicable, art. 293 B du CGI" sur tes factures/reçus.
- Au-delà de ce seuil (vérifie le montant en vigueur sur **impots.gouv.fr**), tu dois collecter et reverser la TVA, avec déclarations périodiques.

## 3. Mentions obligatoires sur le site

- **Mentions légales** (page dédiée) : nom et statut de l'entreprise, numéro SIRET, adresse, moyen de contact, hébergeur du site (pour un thème Shopify : Shopify Inc./Shopify International Limited, dont les coordonnées figurent dans les CGU de Shopify).
- **CGV (Conditions Générales de Vente)** : obligatoires pour toute vente en ligne à des particuliers — droit de rétractation (14 jours, avec les exceptions légales, ex. produits d'hygiène descellés type shampoing/produits alimentaires ouverts), modalités et délais de livraison, garanties légales (conformité, vices cachés), modalités de paiement et de remboursement.
- **Politique de confidentialité / RGPD** : ce que tu collectes (email, adresse, données de paiement traitées par Shopify/Stripe), pourquoi, combien de temps, comment un client peut demander l'accès ou la suppression de ses données.
- **Bandeau cookies** si tu utilises des outils de tracking (Meta Pixel, Google Tag — voir `accelerer-acquisition-clients.md`) : consentement à recueillir avant dépôt de cookies non essentiels.

Shopify propose des générateurs de base pour ces pages dans **Paramètres → Règles** — utile comme point de départ, mais à adapter à ta situation réelle plutôt qu'à garder tel quel.

## 4. Facturation

- Toute vente à un client doit pouvoir donner lieu à une facture/reçu conforme (mentions : identité de l'entreprise, SIRET, numéro séquentiel, détail TVA le cas échéant). Shopify génère les reçus de commande automatiquement ; vérifie qu'ils contiennent bien ces mentions une fois ton statut créé.
- Les obligations de facturation électronique évoluent régulièrement en France (réforme en cours pour les échanges B2B) — pas d'impact immédiat pour de la vente aux particuliers (B2C), mais à surveiller si tu factures aussi des professionnels (ex. un partenariat avec un toiletteur/vétérinaire).

## 5. Spécifique à l'alimentation animale

Déjà détaillé dans `supplier-sourcing-alibaba-guide.md` : les croquettes/friandises sont des aliments pour animaux soumis à une réglementation d'hygiène et d'étiquetage spécifique (DGCCRF), distincte des accessoires. À vérifier avant de lister ces produits, particulièrement si tu passes en achat en gros plutôt qu'en dropshipping.

## 6. Assurance

Une **assurance responsabilité civile professionnelle** est recommandée (pas systématiquement obligatoire selon le statut et l'activité) — utile en cas de litige client ou de produit défectueux. À vérifier avec ton assureur/expert-comptable au moment de la création du statut.

## Ordre pratique

1. Immatriculation (statut auto-entrepreneur) — avant toute vente, même via le lien Stripe rapide.
2. Vérifier le seuil de franchise TVA applicable à ton activité.
3. Générer/adapter mentions légales + CGV + politique de confidentialité dans Shopify.
4. Vérifier la réglementation alimentation animale si tu listes croquettes/friandises.
5. Consulter un expert-comptable pour valider l'ensemble avant le lancement officiel.
