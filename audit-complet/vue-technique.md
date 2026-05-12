---
title: Vue Technique
description: "Chantiers techniques, architecture et checklist d'implémentation pour l'équipe de développement (CTO, Lead Dev)."
---

# Vue Technique (CTO & Dev)

Cette vue est destinée aux équipes techniques responsables de l'implémentation. Elle liste les chantiers prioritaires, les évolutions d'architecture et les points de vigilance.

## 🏗️ Architecture Cible

L'objectif est d'évoluer vers une architecture composable et automatisée :
- **Core E-commerce** : Odoo Shop Invaders (existant).
- **Contenu & Blog** : CMS Headless (ex: Strapi, Sanity) pour une gestion découplée.
- **Automatisation IA** : Serveur MCP (Model Context Protocol) connecté à Odoo, Klaviyo et au CMS Headless.

## ✅ Checklist Technique

### Anomalies Critiques (Priorité Haute)
- [ ] Créer et configurer le fichier `robots.txt` (actuellement vide) pour préserver le budget crawl.
- [ ] Corriger la balise `<link rel="canonical">` sur les pages paginées (`?page=X` pointe actuellement vers la page 1).
- [ ] *Détails : [Anomalies Techniques Critiques](anomalies-techniques.md)*

### Optimisations On-Site (Priorité Moyenne)
- [ ] Déployer les données structurées JSON-LD (`ProductGroup`, `CollectionPage`, `AggregateRating`, `BreadcrumbList`, etc.).
- [ ] Corriger le Cumulative Layout Shift (CLS) en utilisant la propriété CSS `aspect-ratio` sur les images.
- [ ] Implémenter une pagination "Degraded Gracefully" (liens HTML standards en plus du chargement JS).
- [ ] Améliorer l'accessibilité WAI-ARIA (viser le niveau AA, le AAA étant trop coûteux à maintenir).
- [ ] *Détails : [Fiches produits](strategie-seo/fiches-produits.md) / [Pages Univers & Catégories](strategie-seo/pages-univers-categories.md)*

### Architecture & Automatisation (Priorité Long Terme)
- [ ] Mettre en place le CMS Headless pour la gestion du blog et des pages pSEO.
- [ ] Déployer et configurer le serveur MCP sur l'infrastructure Odoo.
- [ ] Connecter le serveur MCP officiel de Klaviyo pour l'automatisation de l'e-mailing.
- [ ] *Détails : [Méthodologie de Déploiement & Automatisation (MCP)](methodologie-mcp.md)*

## ⚠️ Risques & Points de Vigilance

- **Budget Crawl** : Ne pas laisser Googlebot s'épuiser sur les URLs à facettes ou le tunnel de commande.
- **Sécurité MCP** : S'assurer que l'agent IA dispose de permissions strictement limitées (moindre privilège) lors de ses interactions avec l'ERP.
- **Performance (Core Web Vitals)** : Surveiller l'impact du JS et des images sur les temps de chargement, particulièrement sur mobile.
