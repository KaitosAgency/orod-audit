---
title: Vue Technique
description: "Chantiers techniques, architecture et checklist d'implémentation pour l'équipe de développement (CTO, Lead Dev)."
---

# Vue Technique (CTO & Dev)

Cette vue est destinée aux équipes techniques responsables de l'implémentation. Elle liste les chantiers prioritaires, les évolutions d'architecture et les points de vigilance.

## Architecture Cible

L'objectif est d'évoluer vers une architecture composable et automatisée :
- **Core E-commerce** : Odoo Shop Invaders (existant).
- **Contenu & Blog** : CMS Headless (ex: Strapi, Sanity) pour une gestion découplée.
- **Acquisition pSEO** : Micro-service dédié (ne pas héberger les dizaines de milliers de pages locales dans le blog) avec son propre sitemap (`sitemap-local.xml`).
- **Automatisation IA** : Serveur MCP (Model Context Protocol) connecté à Odoo, Klaviyo et au CMS Headless. Il est explicitement recommandé d'utiliser le module **MuK MCP** sur Odoo (plutôt que des briques OCA en PoC).

## Checklist Technique

### Anomalies Critiques & Crawl (Priorité Haute)
- [ ] Configurer le `robots.txt` : `Disallow` sur les facettes (`univers`, `taille`, `couleur`, `prix`), `/account`, `/cart`, `/checkout`, `/api/`. Déclarer le `Sitemap` officiel.
- [ ] Corriger la balise `<link rel="canonical">` sur les pages paginées (`?page=X` pointe actuellement vers la page 1).
- [ ] Implémenter une pagination "Degraded Gracefully" (liens HTML standards en plus du chargement JS).
- [ ] *Détails : [Anomalies Techniques Critiques](anomalies-techniques.md) / [Pages Univers & Catégories](strategie-seo/pages-univers-categories.md)*

### Sémantique, Balisage & URLs (Priorité Moyenne)
- [ ] **Sémantique HTML** : Utiliser la balise `<nav>` pour le menu principal.
- [ ] **Open Graph** : Passer de `og:type=website` à `og:type=product` sur les fiches produits.
- [ ] **URLs propres** : Créer des slugs standards (`/contact`, `/qui-sommes-nous`, `/zones-d-intervention` pour le hub pSEO) et mettre en place des redirections 301 depuis les anciennes URLs.
- [ ] *Détails : [Menu & Navigation](strategie-seo/menu-navigation.md) / [Éléments Transverses](strategie-seo/elements-transverses.md)*

### Déploiement JSON-LD (Données Structurées)
- [ ] **E-commerce** : `ProductGroup`, `CollectionPage`, `AggregateRating`, `BreadcrumbList`.
- [ ] **Navigation & Grilles** : `SiteNavigationElement` (menu), `ItemList` (généré directement dans le composant grille produit/blog).
- [ ] **Contenu & Marque** : `Article`/`BlogPosting`, `Person` (auteurs), `VideoObject`, `FAQPage` (via `<details>/<summary>`).
- [ ] **Institutionnel** : `Organization`/`AboutPage`, `ContactPage`, `Service`.
- [ ] *Détails : [Fiches produits](strategie-seo/fiches-produits.md) / [Pages Univers & Catégories](strategie-seo/pages-univers-categories.md) / [Éléments Transverses](strategie-seo/elements-transverses.md)*

### Performance & Accessibilité (Core Web Vitals)
- [ ] **Optimisation Images** : WebP, `srcset`, `loading="lazy"`.
- [ ] **CLS (Cumulative Layout Shift)** : Fixer les ratios d'images en utilisant la propriété CSS `aspect-ratio` ou les attributs `width`/`height`.
- [ ] **Accessibilité WAI-ARIA** : Viser le niveau AA (le AAA étant trop coûteux à maintenir) en ajoutant les rôles et attributs `aria-*` sur les menus, modales et facettes.
- [ ] *Détails : [Fiches produits](strategie-seo/fiches-produits.md) / [Pages Univers & Catégories](strategie-seo/pages-univers-categories.md)*

### Architecture & Automatisation (Priorité Long Terme)
- [ ] Mettre en place le CMS Headless pour la gestion du blog et le micro-service pour les pages pSEO.
- [ ] Déployer le module **MuK MCP** sur l'infrastructure Odoo.
- [ ] Connecter le serveur MCP officiel de Klaviyo pour l'automatisation de l'e-mailing.
- [ ] *Détails : [Méthodologie de Déploiement & Automatisation (MCP)](methodologie-mcp.md)*

## Risques & Points de Vigilance

- **Budget Crawl** : Ne pas laisser Googlebot s'épuiser sur les URLs à facettes ou le tunnel de commande (spider trap).
- **Sécurité MCP** : S'assurer que l'agent IA dispose de permissions strictement limitées (moindre privilège) lors de ses interactions avec l'ERP.
- **Performance (Core Web Vitals)** : Surveiller l'impact du JS et des images sur les temps de chargement, particulièrement sur mobile.
