---
title: Vue Contenu
description: "Lignes directrices, templates et calendrier pour l'équipe éditoriale et les rédacteurs."
---

# Vue Contenu (Éditorial & Rédaction)

Cette vue est destinée aux équipes en charge de la création de contenu (rédacteurs, responsables communication). Elle définit le ton, les formats attendus et le rythme de publication.

## Lignes Directrices Éditoriales

- **Ton de voix** : Professionnel, expert, rassurant (B2B/B2G). Éviter le jargon inutile mais utiliser les termes techniques précis du métier (normes, matériaux).
- **Cible** : Acheteurs institutionnels, responsables achats, mairies (Police Municipale), professionnels de la sécurité.
- **E-E-A-T** : Toujours mettre en avant l'expertise d'OROD (années d'expérience, conformité aux normes, acceptation Chorus Pro). Utiliser de vrais auteurs pour le blog (pas de "faux experts") avec une page auteur dédiée et un lien vers leur profil LinkedIn (`sameAs`).

## Checklist Éditoriale

### Pages Catégories E-commerce (Les 115 Silos)
- [ ] Rédiger un texte d'introduction (Hero) impactant sous le H1 (possibilité de texte plus long avec une troncature UX `line-clamp` pour ne pas repousser les produits).
- [ ] Rédiger un texte SEO de bas de page **très riche (1500 à 3000 mots)** structuré avec des H2/H3 fréquents et une troncature UX.
- [ ] Intégrer une section FAQ (Foire Aux Questions) pertinente pour chaque catégorie.
- [ ] *Détails : [Pages Univers & Catégories](strategie-seo/pages-univers-categories.md)*

### Fiches Produits
- [ ] S'assurer que les descriptions produits sont uniques (éviter le duplicate content fournisseur).
- [ ] Structurer la page avec un texte SEO de **300 à 500 mots (dépliable)** en bas de page.
- [ ] Intégrer des vidéos de démonstration (qui seront balisées avec `VideoObject`).
- [ ] Utiliser un menu d'ancres interne (Description / Avis / Specs / Livraison).
- [ ] Optimiser les attributs `alt` des images avec des descriptions claires (ex: "Polo Police Municipale manches courtes").
- [ ] *Détails : [Fiches produits](strategie-seo/fiches-produits.md)*

### Le Blog (Tunnel de Vente)
- [ ] **Pages catégories du blog** : Rédiger une intro courte (150-300 mots) pour éviter la cannibalisation avec les catégories e-commerce.
- [ ] **Articles Guides (Type 1)** : 1000 à 1500 mots pour répondre à des questions précises.
- [ ] **Articles Listicles (Type 2)** : 1500 à 2500 mots (idéal pour le GEO), en plaçant toujours un produit OROD en #1.
- [ ] Respecter le rythme : 1 article par jour pendant 3 à 6 mois, puis 3 à 4 articles par semaine.
- [ ] *Détails : [Stratégie Éditoriale & Blog](strategie-editoriale-et-blog.md)*

### Pages Institutionnelles & Lead Gen
- [ ] **Page "Qui sommes-nous"** : Rédiger un storytelling fort, lister les normes/décrets respectés, intégrer des photos des locaux et de l'équipe.
- [ ] **Captation d'e-mails** : Rédiger les accroches pour les pop-ups (scroll/exit-intent), les encarts de fin d'article de blog, et la page de téléchargement du catalogue PDF.
- [ ] *Détails : [Éléments Transverses](strategie-seo/elements-transverses.md)*

### E-mailing & Fidélisation
- [ ] Préparer les templates d'e-mails automatisés (Bienvenue, Panier abandonné, Demande d'avis).
- [ ] Rédiger les campagnes promotionnelles (Hero Banner) en batching.
- [ ] *Détails : [Fidélisation & E-mailing](fidelisation-emailing.md)*

## Organisation & Batching

Pour tenir le rythme, l'approche recommandée est le **batching** (production par lots) couplée à l'assistance de l'IA (via le serveur MCP) pour la génération des premiers jets, qui seront ensuite validés et enrichis par l'équipe éditoriale.
