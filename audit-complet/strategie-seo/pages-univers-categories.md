---
title: Pages Univers & Catégories
---

# Pages Univers & Catégories

## Optimisation des Métadonnées (Title, Description, JSON-LD)

**Constat sur la page Univers "Police Municipale" :**

* **URL :** `https://orod.fr/univers/police-municipale`
* **Balise Title :** `<title>Police Municipale | OROD</title>`
* **Meta Description :** `<meta name="description" content="Concevoir, équiper et accompagner, durablement, ceux qui nous protègent.">`
* **Balise Canonical :** Bien configurée vers l'URL propre.

**Analyse et Recommandations SEO :**

1. **Balise Title (Trop courte et sous-optimisée) :**
   * _Le problème :_ Le Title actuel ("Police Municipale | OROD") est beaucoup trop basique. Il manque d'intention commerciale et de mots-clés secondaires (longue traîne).
   * _La solution :_ Utiliser les 60 caractères disponibles pour intégrer le type de produits vendus.
   * _Exemple recommandé :_ `<title>Équipements et Uniformes Police Municipale | OROD</title>`
2. **Meta Description (Générique et dupliquée) :**
   * _Le problème :_ La meta description actuelle est le slogan global de l'entreprise. Elle est probablement identique sur toutes les pages catégories du site. Google déteste les meta descriptions dupliquées et finira par les ignorer.
   * _La solution :_ Chaque catégorie doit avoir une description unique, incitant au clic, qui décrit exactement ce qu'on va trouver sur la page.
   * _Exemple recommandé :_ `<meta name="description" content="Découvrez notre gamme complète d'équipements pour la Police Municipale : uniformes réglementaires, gilets pare-balles et accessoires tactiques.">`
3. **Données Structurées JSON-LD (Basiques et incomplètes) :**
   * _Le problème :_ L'analyse du code montre un JSON-LD très pauvre pour une page e-commerce. Il déclare simplement qu'il s'agit d'une page web (`WebPage`) appartenant à une organisation (`Organization`). **Il manque plusieurs éléments cruciaux :** le fil d'Ariane (`BreadcrumbList`), la déclaration de type de page (`CollectionPage` au lieu du générique `WebPage`), la liste des produits (`ItemList`), et les avis globaux de la catégorie (`AggregateRating`).
   * _La solution :_
     * Changer le type `@type` de `WebPage` à `CollectionPage`.
     * Ajouter le bloc `BreadcrumbList` (comme c'est déjà très bien fait sur les fiches produits).
     * Ajouter dynamiquement un bloc `ItemList` contenant les URLs et noms des produits affichés dans la grille (voir section dédiée plus bas). C'est ce qui indique à Google qu'il explore un catalogue.
     * **Ajouter le bloc `AggregateRating`** : Agréger la note moyenne de tous les produits de cette catégorie pour faire apparaître les étoiles jaunes dans les résultats de recherche (SERP) sur la page catégorie elle-même.

## Création de véritables pages Catégories (Silos SEO)

**Constat :** Le site possède bien des pages "Univers" propres (ex: `/univers/police-municipale`). Cependant, dès que l'on navigue dans les sous-catégories (ex: Uniformes, Hauts) depuis le menu, le site utilise un système de filtres d'URL.

<div align="left"><figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure></div>

_Figure 5 : URL filtrée pour la catégorie Uniformes._

<div align="left"><figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure></div>

_Figure 6 : URL filtrée pour la sous-catégorie Hauts._

**Impact :** Bien que pratique pour l'utilisateur, ce système génère des URLs dynamiques (ex: `?univers=["Police+Municipale"]`) qui sont très mal comprises et indexées par Google. Google préfère les arborescences claires en "Silos" (des dossiers bien rangés).

**Recommandation :**

* **Transformer les filtres en véritables pages (Silos) :** Au lieu de filtrer une page générique "Hauts", il faut créer des pages physiques dédiées à chaque intention de recherche, imbriquées sous leur univers.
  * _Exemple actuel :_ `/uniformes/hauts?univers=["Police+Municipale"]`
  * _Exemple recommandé :_ `/univers/police-municipale/uniformes/polos-chemises-vestes`
* **Volume estimé & Impact Trafic :** L'analyse de l'arborescence actuelle du menu révèle qu'il y a très exactement **115 combinaisons uniques** (ex: ASVP > Défense > Aérosols, Pompiers > Uniformes > Hauts, etc.). Il s'agit donc de créer **115 pages catégories physiques** pour remplacer les filtres actuels. La création de ces 115 pages optimisées (avec leurs propres H1 et textes) va permettre de multiplier par 115 les portes d'entrée vers le site depuis Google. Cela va mécaniquement capter une audience beaucoup plus large sur des requêtes de "longue traîne" très qualifiées (ex: "achat aérosol défense ASVP" au lieu de juste "aérosol").
* **Attention à la sur-optimisation des URLs :** Il n'est pas nécessaire (et même déconseillé) de répéter le mot-clé principal à chaque niveau de l'URL.
  * _Mauvais exemple (Suroptimisé) :_ `/univers/police-municipale/uniformes-police-municipale/polos-police-municipale` (Google y verra du "Keyword Stuffing" ou bourrage de mots-clés).
  * _Bon exemple (Naturel) :_ `/univers/police-municipale/uniformes/polos-chemises` (Le contexte "Police Municipale" est déjà donné par le dossier parent, Google comprend l'héritage sémantique).
* **Distinguer l'URL du contenu (H1 & Title) :** Si l'URL doit rester courte et hiérarchique (ex: `/uniformes`), le contenu de la page, lui, doit être parfaitement explicite.
  * La balise `<title>` et le `<h1>` de cette page devront bien être : **"Uniformes Police Municipale"** (et non pas juste "Uniformes"). C'est là que se joue la vraie optimisation sémantique.
* **Bénéfice :** C'est le cœur de l'optimisation SEO e-commerce. Chaque page aura sa propre URL propre, son propre titre `H1`, sa propre balise `Title` et son propre texte descriptif. C'est indispensable pour se positionner sur des requêtes précises (longue traîne) comme "Achat polo police municipale".

## Enrichissement Éditorial des Univers (Cas Pratique : Police Municipale)

**URL analysée :** `https://orod.fr/univers/police-municipale`

**Constat :** La page ne contient qu'une seule phrase descriptive (_"Équipements complets pour la police municipale : uniformes, gilets pare-balles, accessoires et matériel conforme aux normes en vigueur."_). C'est beaucoup trop "maigre" (Thin Content) pour que Google considère cette page comme une référence. De plus, l'utilisateur fait face à 187 produits mélangés sans accompagnement éditorial ni réassurance.

**Recommandation : Le Gabarit Idéal d'une Page Catégorie (SEO & CRO)**\
Pour transformer cette page "Univers" en une véritable machine à trafic et à conversion, voici la structure idéale à implémenter de haut en bas :

{% stepper %}
{% step %}
**En-tête SEO (Haut de page)**

* Sous le fil d'Ariane, intégrer un **H1 optimisé** (ex: _Équipements et Uniformes Police Municipale_).
* Ajouter un court texte introductif (150-200 mots) avec une image d'illustration. Il doit contenir 2 phrases d'intro, un H2 (ex: _Notre sélection réglementaire_), et 2 autres phrases.
* _Astuce UX / SEO :_ Pour ne pas repousser les produits trop bas (surtout sur mobile), **tronquer visuellement** l'intro à **4 lignes** avec du CSS (`display: -webkit-box`, `-webkit-box-orient: vertical`, `overflow: hidden`, `-webkit-line-clamp: 4`, `text-overflow: ellipsis`). Le texte complet reste dans le HTML : les moteurs indexent l'intégralité du contenu. Ajouter si besoin un bouton « Lire la suite » qui retire la limite ou étend la zone (comportement UX, pas une obligation pour le robot).
{% endstep %}

{% step %}
**Navigation & Filtres (Barre latérale gauche)**

* _Est-ce pertinent ?_ Oui, absolument indispensable pour l'UX quand on a 187 produits. L'utilisateur doit pouvoir filtrer par taille, prix ou type.
* _Titres des groupes de filtres :_ Utiliser des **`<div>`** (ou libellés neutres) pour les intitulés de blocs filtres (ex. « Taille », « Prix »), **sans balises `h2`–`h6`**, afin de ne pas diluer la hiérarchie des titres réservée au contenu éditorial et aux produits.
* _Alerte SEO :_ La navigation à facettes est le plus grand danger en SEO e-commerce. Il faut s'assurer que les URLs générées par ces filtres (ex: `?taille=M&couleur=bleu`) ne soient **pas indexables** par Google (via `robots.txt` ou balise `canonical` vers la catégorie mère) pour éviter la duplication de contenu massive.
{% endstep %}

{% step %}
**Grille Produits & UX**

* Afficher les produits avec les optimisations vues précédemment (marque en badge, survol fluide).
* **Enveloppe sémantique :** Encapsuler **chaque carte produit** dans une balise **`<article>`** (conteneur de la vignette : image, titre, prix, CTA). Au sens HTML5, une carte est une « composition autonome » redistribuable — ce qui correspond exactement à une unité catalogue. Un code clair, sémantique et bien structuré facilite le travail des robots d'indexation et joue en faveur du référencement global.
* **Titres dans les cartes :** Baliser chaque nom de produit en **`<h3>`** (accueil et pages catégories), sous le **`h1`** de la page et les **`h2`** de section — hiérarchie cohérente avec la page d'accueil décrite sur la [Page d'accueil](page-accueil.md).
* **Module "Derniers produits consultés" :** Ajouter cette section en bas de la grille. C'est un levier CRO majeur qui facilite la navigation croisée et augmente le panier moyen.
{% endstep %}

{% step %}
**Preuve Sociale (Avis Clients Catégorie)**

* _Où les placer ?_ Juste sous la grille de produits (et les derniers consultés), avant le gros bloc de texte SEO.
* _Quoi afficher ?_ Un carrousel des meilleurs avis clients concernant spécifiquement les produits de cet univers (ex: avis sur les uniformes PM).
* _L'astuce SEO :_ C'est ici qu'il faut agréger la note globale de la catégorie (ex: 4.8/5 sur 120 avis) et injecter la donnée structurée `AggregateRating` pour faire apparaître les étoiles jaunes directement dans les résultats de recherche Google.
{% endstep %}

{% step %}
**Le Bloc "Texte SEO" (Bas de page)**

* C'est le moteur de votre référencement. Un texte riche de **1500 à 3000 mots**, structuré avec de très nombreux H2 et H3 (règle de rédaction : prévoir un sous-titre H2 ou H3 tous les 70 à 150 mots environ pour aérer la lecture et maximiser les requêtes de longue traîne).
* _Astuce UX / SEO :_ **Ne pas** imposer une hauteur fixe en pixels. Préférer une **troncature à 4 lignes** avec les mêmes propriétés CSS que pour l'en-tête (`-webkit-line-clamp: 4`, ellipse, etc.), le texte complet restant présent dans le DOM pour l’indexation. Offrir un bouton « En savoir plus » / « Déplier » qui retire la limite ou affiche le bloc en entier améliore la lisibilité sans réduire le signal SEO.
{% endstep %}

{% step %}
**FAQ (balises HTML5 + JSON-LD)**

* **Constat sur OROD :** À ce jour, les pages catégories / univers analysées ne comportent pas encore de bloc FAQ structuré en `<details>` / `<summary>` ni de FAQ dédiée alignée avec une donnée structurée FAQ.
* **Recommandation d'intégration :** Intégrer **6 questions fréquentes** liées à l’univers, en utilisant **exclusivement les balises HTML5 natives** : chaque question dans un `<summary>`, la réponse dans le corps du `<details>`.
  * _Pourquoi éviter la méthode "Divs + JS" ?_ Certains sites utilisent des `<div>` avec des attributs `role="button"` et `aria-expanded` gérés par JavaScript pour créer leurs FAQ. Cette méthode est obsolète, alourdit le code et dépend du JS. Les balises natives `<details>`/`<summary>` sont nativement accessibles et lisibles par les robots sans aucun script.
  * _Sémantique :_ Placer la question à l'intérieur d'une balise **`<h3>`** (elle-même dans le `<summary>`) pour structurer la page.
* **Données Structurées :** Dupliquer la même information dans un script **JSON-LD `FAQPage`** séparé dans le `<head>`. Il faut absolument **fuir les Microdonnées en ligne** (attributs `itemprop`, `itemscope` directement dans le HTML) qui alourdissent considérablement le DOM et rendent la maintenance difficile. Le JSON-LD est le standard asynchrone recommandé par Google.
{% endstep %}

{% step %}
**Maillage Éditorial (Blog)**

* Afficher les 3 ou 4 derniers articles de blog **spécifiques à cet univers**. Cela crée un "Cocon Sémantique" parfait aux yeux de Google (la page de vente fait des liens vers les pages conseils, et inversement).
* Titres des cartes / vignettes blog sur ces blocs : balises **`<h3>`**.
{% endstep %}

{% step %}
**Bandeau de Réassurance**

* Juste avant le footer, rappeler les éléments de confiance : Livraison, Paiement sécurisé (Chorus Pro), Service client.
{% endstep %}

{% step %}
**Affichage responsive (Mobile-First)**

* Il est acceptable d’utiliser des **classes CSS** pour masquer ou réordonner des blocs selon la viewport (ex. équivalents de `hidden-mobile`, `desktop-only`, `mobile-only`), tant que **le même HTML** est servi à tous les utilisateurs. Cela reste aligné avec une indexation **mobile-first** tant qu’on ne sert pas un contenu différent selon le user-agent pour tromper les moteurs (à distinguer du simple responsive par CSS).
{% endstep %}
{% endstepper %}

## Pagination & Scroll Infini (Le piège UX / SEO)

**Constat :** Les pages catégories d'OROD utilisent un système de chargement des produits au fur et à mesure de la descente (Scroll Infini), tout en générant des URLs paginées (ex: `?page=3`).

**Le problème du "Footer Inaccessible" :** Le scroll infini automatique est un faux-ami en e-commerce. Si les produits se chargent indéfiniment, l'utilisateur ne peut **jamais** atteindre le bas de la page. Conséquence dramatique : le bloc d'Avis Clients, le texte SEO (Guide d'achat) et le Footer (avec tous ses liens de réassurance et de maillage) deviennent totalement inaccessibles pour un humain.

**Recommandations UX & SEO :**

1. **Remplacer le Scroll Infini par un bouton "Charger la suite" :** C'est la meilleure pratique e-commerce actuelle, particulièrement optimisée pour la navigation mobile. Au lieu de charger automatiquement, affichez un gros bouton "Voir X produits suivants". Cela permet à l'utilisateur qui le souhaite de faire défiler la page jusqu'en bas pour lire les avis ou le texte SEO, sans être interrompu par l'apparition forcée de nouveaux produits.
2. **⚠️ Alerte SEO Critique sur la balise Canonical (`?page=X`) :** L'analyse en direct de l'URL `https://orod.fr/uniformes?page=3` révèle une **erreur SEO majeure**. Actuellement, la balise canonical de la page 3 pointe vers la page 1 (`<link rel="canonical" href="https://orod.fr/uniformes">`).
   * _L'impact :_ En faisant cela, on dit à Google : "La page 3 est un simple doublon de la page 1, ne l'indexe pas". Conséquence directe : Google n'explorera et n'indexera **jamais** les produits qui se trouvent sur les pages 2, 3, 4, etc. Une grande partie du catalogue est donc invisible pour les moteurs de recherche.
   * _La solution absolue :_ Il faut modifier le code pour qu'une page paginée pointe vers **elle-même**. La balise canonical de la page 3 doit être `<link rel="canonical" href="https://orod.fr/uniformes?page=3">`. C'est vital pour l'indexation profonde du catalogue.
3. **Maillage HTML pour les robots (Le compromis UX/SEO) :** C'est le point le plus technique mais le plus crucial.
   * _Le problème :_ L'humain aime cliquer sur "Charger la suite" pour voir les produits apparaître de manière fluide (Javascript). Mais le robot Google, lui, ne sait pas cliquer sur ce bouton. Il a besoin d'un vrai lien vers une "Page 2" pour continuer son exploration.
   * _La solution technique (à transmettre aux développeurs) :_ Il faut utiliser la méthode de la **"Pagination dégradée gracieusement"**. Le bouton "Charger la suite" doit être, dans le code HTML, un véritable lien vers la page suivante (`<a href="?page=2">Charger la suite</a>`).
     * Quand un **humain** clique dessus, le Javascript intercepte le clic, bloque le changement de page, et affiche les produits de manière fluide.
     * Quand un **robot** (qui n'exécute pas ce Javascript) "clique" dessus, il suit le lien HTML normal et arrive sur l'URL `?page=2`, où il trouve la suite du catalogue.
   * _La limite de pages :_ Le système CMS (Odoo) sait automatiquement combien de produits il y a dans la catégorie. S'il y a 100 produits affichés par 20, il générera un lien vers la page 2, puis sur la page 2 un lien vers la page 3, jusqu'à la page 5 où le bouton "Charger la suite" disparaîtra. Il n'y a donc pas de risque de générer "50 000 pages" infinies.

## Templates de Rédaction Industrialisés (Pages Catégories & FAQ)

Pour gagner du temps et garantir une cohérence SEO sur les 115 pages catégories potentielles, voici des gabarits (templates) à fournir aux rédacteurs. Ils sont conçus pour intégrer naturellement les mots-clés tout en répondant aux exigences des professionnels de la sécurité.

**1. Template du Texte Introductif (Haut de page - 100 à 150 mots)**\
\&#xNAN;_Objectif : Accrocher l'utilisateur, placer le mot-clé principal (H1) et rassurer immédiatement. Le rédacteur devra faire preuve de créativité pour éviter la duplication._

* **H1 :** Mot-clé principal (Type d'équipement + Univers métier).
* **Phrase 1 (L'accroche métier) :** Intégration naturelle du mot-clé principal et ciblage des exigences spécifiques de l'univers métier.
* **Phrase 2 (La promesse technique) :** Mise en avant des matériaux, du confort et de la durabilité.
* **Phrase 3 (L'appel à l'action) :** Invitation à parcourir le catalogue et à utiliser les filtres.

**2. Template du Texte SEO Long (Bas de page - 1500 à 3000 mots)**\
\&#xNAN;_Objectif : Créer un contenu exhaustif pour capter la longue traîne SEO, asseoir l'expertise E-E-A-T d'OROD et développer un champ sémantique riche, sans brider la créativité du rédacteur avec une structure figée._

* **Volume et densité :** Pour atteindre les **1500 à 3000 mots** sans faire de "remplissage" (fluff), il est impératif de développer en profondeur le champ lexical spécifique à chaque catégorie.
* **Règle d'or de structuration :** Insérer un sous-titre (H2 ou H3) tous les **70 à 150 mots environ**. Cela permet de maintenir l'attention du lecteur tout en multipliant les points d'entrée SEO.
* **Thématiques à explorer :** Le rédacteur devra construire son propre plan pour chaque catégorie en s'assurant d'aborder les critères de choix, la réglementation en vigueur, les spécificités techniques des matériaux, et les différents types de produits disponibles pour cet univers métier.

_🤖 **Astuce de production :** Rédiger des centaines de textes pour les catégories et les fiches produits est un chantier colossal. Cette phase sera **industrialisée via mes outils d'Intelligence Artificielle et mon serveur MCP** connectés à votre ERP Odoo (voir la page_ [_Méthodologie de Déploiement_](../methodologie-mcp.md)_)._

**3. Template de FAQ (Foire Aux Questions)**\
\&#xNAN;_Objectif : Capter les positions "People Also Ask" (Autres questions posées) sur Google et lever les derniers freins à l'achat._

* **Volume attendu :**
  * **6 questions** pour les pages **Catégories**.
  * **8 questions** pour les pages **Produits**.
* **Thématiques à couvrir par le rédacteur :** C'est sur cette phase que la qualité du rédacteur (ou du prompt IA) fera la différence. Les questions doivent être de véritables requêtes utilisateurs et couvrir :
  * Les aspects réglementaires et légaux.
  * Les aspects techniques, de taillage et d'ergonomie.
  * Les conseils d'entretien pour la durabilité.
  * Les questions administratives et logistiques (mandats, livraisons).

## Stratégie de Maillage Interne (Pages Catégories)

Pour maximiser la distribution du "jus SEO" (PageRank) et aider Google à comprendre l'architecture en silos d'OROD, le maillage interne des pages catégories doit être pensé de manière multidirectionnelle. Il ne s'agit pas de faire de simples listes à puces en bas de page, mais d'**intégrer ces liens naturellement au cœur du texte SEO** (dans les 1500-3000 mots).

Voici la structure de maillage recommandée pour chaque page catégorie :

1. **Maillage Ascendant (Vers la catégorie parente) :**
   * _Objectif :_ Renforcer la puissance de la page "Univers" principale.
   * _Méthode :_ En plus du fil d'Ariane, faire un lien contextuel vers l'univers parent.
   * _Exemple (sur la page Polos PM) :_ "Découvrez comment ce polo s'intègre parfaitement à votre tenue complète de [Police Municipale](./#lien-univers-pm)."
2. **Maillage Descendant (Vers les catégories enfants) :**
   * _Objectif :_ Pousser le robot Google à explorer les pages profondes (longue traîne).
   * _Méthode :_ Si la catégorie possède des sous-catégories, faire des liens vers celles-ci.
   * _Exemple (sur la page Uniformes PM) :_ "Notre gamme se décline en [polos et t-shirts](./#lien-enfant), mais également en [pantalons d'intervention](./#lien-enfant)."
3. **Maillage Transversal (Vers la catégorie "non-univers" correspondante) :**
   * _Objectif :_ Relier les "Silos Métiers" aux "Silos Produits" globaux.
   * _Méthode :_ Faire un lien vers le catalogue générique du même type de produit.
   * _Exemple (sur la page Polos PM) :_ "Vous cherchez d'autres modèles ? Consultez l'ensemble de notre catalogue de [polos tactiques et professionnels](./#lien-polos-generiques)."
4. **Maillage Latéral (Vers les "Catégories Sœurs" du même univers) :**
   * _Objectif :_ Créer un Cocon Sémantique parfait en gardant le robot enfermé dans l'univers métier.
   * _Méthode :_ Lier les catégories de même niveau pour "compléter la tenue".
   * _Exemple (sur la page Polos PM) :_ "Pour garantir votre sécurité sur le terrain, nos polos s'intègrent parfaitement sous nos [gilets pare-balles Police Municipale](./#lien-soeur), et peuvent être associés à notre gamme de [pantalons d'intervention tactiques](./#lien-soeur)."
5. **Maillage Profond Direct (Vers le Top 3 Produits) :**
   * _Objectif :_ Transférer l'autorité de la catégorie directement vers les fiches produits qui rapportent le plus de chiffre d'affaires (Best-sellers).
   * _Méthode :_ Citer explicitement les produits phares dans le texte avec un lien direct vers leur fiche.
   * _Exemple :_ "Parmi nos modèles les plus plébiscités, le [Polo Airflow Thermorégulant](./#lien-produit) se distingue par sa légèreté."
6. **Maillage Éditorial (Vers le Blog) :**
   * _Objectif :_ Valider l'expertise (E-E-A-T) en liant les pages transactionnelles aux pages informationnelles.
   * _Méthode :_ Faire un lien vers un article de blog qui traite spécifiquement de cette catégorie.
   * _Exemple :_ "Vous hésitez entre plusieurs modèles ? Consultez notre guide complet pour [bien choisir son uniforme de Police Municipale](./#lien-blog)."

## Accessibilité (WAI-ARIA) — Un code clair pour les robots et les utilisateurs

Bien que l'accessibilité (WAI-ARIA) soit avant tout destinée aux utilisateurs naviguant avec des lecteurs d'écran (conformité RGAA / WCAG), un code enrichi et structuré de la sorte est un signal extrêmement positif pour Google. Un code clair, qui décrit parfaitement la fonction de chaque élément (un bouton, une modale, un menu déroulant), facilite le "crawl" (l'exploration) par les robots et s'inscrit dans la volonté de Google de valoriser les sites offrant une expérience utilisateur (UX) irréprochable.

**Objectif recommandé : Le niveau AA (WCAG / RGAA)**\
Pour un site e-commerce comme OROD, l'objectif stratégique idéal est le **niveau AA**. Il permet d'obtenir 95% des bénéfices SEO de l'accessibilité (code propre, balises sémantiques, attributs alt, navigation claire) sans sacrifier le design, l'image de marque et la conversion. Viser le niveau AAA (qui impose des contrastes extrêmes de 7:1 et l'interdiction totale de texte dans les images) est déconseillé car cela dégraderait l'aspect visuel du site et pourrait impacter négativement les ventes, sans apporter de bonus SEO supplémentaire de la part de Google.

**Constat sur la page d'accueil d'OROD :**\
L'analyse du code source de la page d'accueil montre que **de très bonnes pratiques d'accessibilité sont déjà en place**. On retrouve un usage pertinent des attributs ARIA pour guider les lecteurs d'écran et les robots :

* `aria-label` est correctement utilisé sur les liens des réseaux sociaux ("Facebook", "Instagram", "LinkedIn").
* `aria-hidden="true"` est présent (probablement pour masquer des icônes décoratives).
* `aria-current="page"` est utilisé pour indiquer la page active.
* Les rôles `role="tab"` et `role="tablist"` sont implémentés pour structurer les éléments de navigation par onglets.

Ces éléments constituent une excellente base de niveau A/AA qu'il convient de maintenir et d'étendre sur les nouveaux développements.

**Priorités métier e-commerce pour consolider le niveau AA sur OROD :**

* **Fil d’Ariane :** `<nav aria-label="Fil d'Ariane">` (libellé en français clair).
* **Recherche :** formulaire principal avec **`role="search"`** (ou équivalent sémantique selon le framework).
* **FAQ (blocs `<details>` / `<summary>`) :** option pour annoncer une liste de questions : conteneur avec **`role="list"`** et chaque **`details`** avec **`role="listitem"`**.
* **Carrousels (produits, destockage, etc.) :** région avec **`aria-live="polite"`** ou **`assertive`** sur la zone qui annonce le changement de slide ; boutons « précédent / suivant » avec **`aria-label`**, **`aria-controls`** pointant vers l'`id` du viewport ; **`aria-disabled`** selon l’état ; slides hors champ avec **`aria-hidden="true"`** ; slides visibles en **`role="group"`** avec **`aria-label`** incluant la position (ex. « 2 sur 5 »).
* **Modales / pop-ups marketing :** **`role="dialog"`**, **`aria-modal="true"`**, titre accessible via **`aria-labelledby`** (lié au `h2` interne) ou **`aria-label`** ; bouton fermeture avec **`aria-label="Fermer"`** ; premier focus dans la modale.
* **Icônes décoratives (Font Awesome, SVG inline) :** **`aria-hidden="true"`** pour ne pas les faire annoncer à la place du texte visible par les lecteurs d'écran.
* **Liens ou boutons icône seuls** (panier, compte, home logo cliquable sans texte visible) : **`aria-label`** descriptif en français.
* **Champs formulaire catalogue** (tri, facettes, déclinaisons sur grille) : **`aria-label`** sur les `<select>` ou composants custom tant que le libellé visible n’est pas correctement relié avec `<label for="…">`.

**Inventaire des attributs `aria-*` essentiels à implémenter sur les composants d'OROD :**

| Attribut            | Exemple d’usage                                                                                                            |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **`aria-label`**    | Boutons carrousel, recherche, ajout au panier, navigation icône, fermeture modale.                                         |
| **`aria-hidden`**   | Icônes décoratives, séparateurs visuels, SVG non porteurs de sens, slides masqués.                                         |
| **`aria-live`**     | Zone de statut recherche (`polite`), zone de notification carrousel (`assertive`), résultat d'action dynamique (`polite`). |
| **`aria-atomic`**   | Annonce complète du contenu mis à jour dans une région live (ex. notification carrousel).                                  |
| **`aria-disabled`** | Boutons flèches désactivés en fin de carrousel.                                                                            |
| **`aria-controls`** | Boutons prev/next du carrousel liés au `id` du wrapper des slides.                                                         |
| **`aria-modal`**    | Fenêtres dialogue pop-in.                                                                                                  |
| **`aria-expanded`** | Menus déroulants, accordéons, panneaux filtres mobile (ouvert/fermé).                                                      |
| **`aria-current`**  | Élément actif du fil d’Ariane ou menu (`page`, `step`, ou `true`).                                                         |
| **`aria-busy`**     | Grille produits ou facettes en cours de rechargement AJAX.                                                                 |
| **`aria-invalid`**  | Formulaires compte, contact, checkout (erreur de saisie).                                                                  |

**Rôles WAI-ARIA (`role`) souvent associés** (non préfixés par `aria-`) : `navigation`, `search`, `main`, `button`, `dialog`, `region`, `group`, `status`, `presentation`, `list`, `listitem`. À utiliser pour préciser la fonction d'un bloc lorsque le HTML natif ne suffit pas.
