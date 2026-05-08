# Anomalies Techniques Critiques

## 2. Anomalies Techniques Critiques

### 2.1 Fichier Robots.txt

**Constat :** Le fichier est vide. Il ne donne aucune instruction aux moteurs de recherche.\
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
* **Prévention du "Spider Trap" (Filtres) :** En e-commerce, la navigation à facettes génère des milliers de combinaisons d'URLs (ex: polo bleu + taille M). **Attention : même si ces pages possèdent une balise `canonical` vers la catégorie mère, cela ne suffit pas.** Pour lire la balise canonical, Google doit d'abord télécharger la page, ce qui épuise inutilement son budget de crawl. Le `Disallow: /*?*...` dans le robots.txt lui interdit carrément l'accès, forçant le robot à ignorer ces pages inutiles pour se concentrer sur le contenu à forte valeur ajoutée.
* **Découverte facilitée :** La ligne `Sitemap` indique immédiatement aux moteurs de recherche (et aux IA) où trouver le plan officiel de votre site pour une indexation rapide.

