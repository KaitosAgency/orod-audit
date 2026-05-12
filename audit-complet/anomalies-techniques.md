---
title: Anomalies Techniques Critiques
description: "Identification et correction des freins techniques majeurs (indexation, pagination, robots.txt) qui bloquent le référencement."
---

# Anomalies Techniques Critiques

## Fichier Robots.txt

**Constat :** Le fichier est vide. Il ne donne aucune instruction aux moteurs de recherche.

**Proposition de contenu pour `https://orod.fr/robots.txt` :**

```
User-agent: *
Allow: /

# Exclusion des pages privées ou inutiles au SEO
Disallow: /account
Disallow: /cart
Disallow: /checkout
Disallow: /api/

# Blocage de la navigation à facettes (filtres) pour éviter le contenu dupliqué
Disallow: /*?*univers=
Disallow: /*?*taille=
Disallow: /*?*couleur=
Disallow: /*?*prix=
# (À adapter avec les paramètres exacts utilisés par le système de filtres)

Sitemap: https://orod.fr/sitemap.xml
```

**Pourquoi cette configuration ?**

* **Optimisation du "Budget de Crawl" :** Google alloue un temps limité à l'exploration de votre site. Bloquer les pages privées ou transactionnelles (`/cart`, `/account`, `/checkout`) force les robots à se concentrer uniquement sur les pages qui ont une valeur SEO (Catégories, Produits, Blog).
* **Prévention du "Spider Trap" (Filtres) :** En e-commerce, la navigation à facettes génère des milliers de combinaisons d'URLs (ex: polo bleu + taille M).\
  \
  ⚠️ **Attention : même si ces pages possèdent une balise `canonical` vers la catégorie mère, cela ne suffit pas.**\
  Pour lire la balise canonical, Google doit d'abord télécharger la page, ce qui épuise inutilement son budget de crawl. Le `Disallow: /*?*...` dans le robots.txt lui interdit carrément l'accès, forçant le robot à ignorer ces pages inutiles pour se concentrer sur le contenu à forte valeur ajoutée.
* **Découverte facilitée :** La ligne `Sitemap` indique immédiatement aux moteurs de recherche (et aux IA) où trouver le plan officiel de votre site pour une indexation rapide.

## Erreur d'URL Canonique sur la Pagination

**Constat :** L'analyse des pages catégories paginées (ex: `https://orod.fr/uniformes?page=3`) révèle une **erreur SEO majeure**. Actuellement, la balise canonical de la page 3 pointe vers la page 1 (`<link rel="canonical" href="https://orod.fr/uniformes">`).

**Impact :** En faisant cela, on indique à Google que la page 3 est un simple doublon de la page 1 et qu'il ne faut pas l'indexer. Conséquence directe : Google n'explorera et n'indexera **jamais** les produits qui se trouvent sur les pages 2, 3, 4, etc. Une grande partie du catalogue profond est donc invisible pour les moteurs de recherche.

**Recommandation :**
Il faut modifier le code pour qu'une page paginée pointe vers **elle-même**. La balise canonical de la page 3 doit être `<link rel="canonical" href="https://orod.fr/uniformes?page=3">`. C'est vital pour l'indexation profonde du catalogue.

*Pour plus de détails sur la gestion de la pagination et du scroll infini, consultez la section dédiée dans [Pages Univers & Catégories](strategie-seo/pages-univers-categories.md).*
