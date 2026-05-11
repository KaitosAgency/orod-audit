---
title: Menu & Navigation
---

# Menu & Navigation

## Sémantique, Accessibilité et Structure HTML du Menu

**Constat :** L'analyse du code source (HTML) révèle plusieurs lacunes concernant la structure du menu :

* Le menu n'utilise pas la balise sémantique HTML5 `<nav>`, mais est encapsulé dans de simples blocs `<div>`.
* La structure est très verbeuse, avec une imbrication excessive de `<div>` autour des listes (`<ul>` et `<li>`), ce qui alourdit l'exploration par les robots de Google.
* Il manque les attributs d'accessibilité (WAI-ARIA) pour indiquer clairement aux moteurs de recherche le comportement des sous-menus.
* **Aucune donnée structurée de type `SiteNavigationElement`** n'est présente pour aider Google à comprendre l'arborescence globale.

<figure><img src="../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

_Figure 4 : Aperçu actuel des Sitelinks sur Google._

**Analyse des Sitelinks actuels :** Bien que Google affiche des sous-liens (Sitelinks), leur sélection est automatique et non maîtrisée. On y trouve des pages pertinentes ("Police Municipale", "Uniformes") mais aussi des pages moins stratégiques ou mal décrites ("Explorez", "Tshirts - Polos" avec une description tronquée sur la newsletter).

**Recommandations pour un menu "10/10" :**

* **Adopter la balise `<nav>` :** Remplacer le bloc principal par une balise `<nav>` avec l'attribut `aria-label="Menu principal"` pour signaler sans ambiguïté la navigation prioritaire.
* **Alléger le code HTML :** Privilégier une structure claire et directe : listes (`<ul>`), éléments (`<li>`) et liens (`<a>`). Supprimer les blocs `<div>` de mise en page inutiles qui entourent actuellement chaque lien.
* **Signaler les sous-menus :** Ajouter les attributs `aria-haspopup` et `aria-expanded` sur les rubriques parentes (comme "Univers"). Cela aide Google (particulièrement en Mobile-First) à comprendre qu'il y a une profondeur de contenu derrière ce clic.
* **Données structurées :** Intégrer un balisage JSON-LD `SiteNavigationElement` afin de lister les rubriques stratégiques et dicter à Google les pages qu'il doit afficher en priorité dans les Sitelinks de recherche.

## Optimisation des Ancres de Liens (Mots-clés du Menu)

**Constat :** Les intitulés du menu (sous-catégories) sont actuellement très génériques (ex: "Hauts", "Bas", "Tête - Coiffes", "Équipements"). Pour Google, le texte d'un lien (l'ancre) est un signal fort pour comprendre le contenu de la page de destination. Un lien "Hauts" n'a aucune valeur SEO.

**Recommandation :**

* **Enrichir les libellés (sans sur-optimiser) :** Remplacer les termes génériques par des mots-clés métier pertinents, mais garder un menu visuellement digeste pour l'utilisateur.
  * _Au lieu de "Hauts" ➔ "Polos, Chemises & Vestes"_
  * _Au lieu de "Bas" ➔ "Pantalons & Bermudas tactiques"_
  * _Au lieu de "Tête - Coiffes" ➔ "Casquettes, Képis & Calots"_
  * _Au lieu de "Équipements" ➔ "Matériel & Équipement Tactique"_
* **Le juste équilibre (Contexte visuel vs SEO) :** Dans un méga-menu classé par univers (ex: une grande colonne "Police Municipale"), il n'est pas nécessaire de répéter "Police Municipale" sur chaque lien enfant. L'utilisateur comprend le contexte visuel.
  * _Ce qu'il faut faire :_ Le lien affiche "Polos, Chemises & Vestes".
  * _L'astuce SEO (Attribut Title) :_ Ajouter un attribut `title` au lien HTML pour donner le contexte complet aux robots de Google : `<a href="/univers/police-municipale/uniformes/polos-chemises" title="Polos et Chemises pour la Police Municipale">Polos, Chemises & Vestes</a>`. Cela permet d'optimiser l'ancre sans alourdir le design du menu.

## Structure des URLs du Menu (Filtres vs URLs propres)

**Constat :** Les liens du menu pointent vers des URLs contenant des paramètres de filtres (ex: `/uniformes/hauts?univers=["Police+Municipale"]`).

**Impact :** Les URLs avec paramètres sont moins bien comprises et indexées par Google que des URLs statiques et propres.

**Recommandation :** Transformer ces liens paramétrés en véritables URLs "propres" (ex: `/police-municipale/uniformes/hauts`). Cela créera de véritables pages "catégories" optimisables pour le SEO.
