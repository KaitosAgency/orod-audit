---
title: Menu & Navigation
---
# Menu & Navigation (Arborescence)

## Sémantique et Données Structurées du Menu

**Constat :** L'analyse du code source révèle que le menu de navigation n'utilise pas la balise sémantique HTML5 `<nav>`, mais de simples `<div>`. De plus, **aucune donnée structurée de type `SiteNavigationElement`** n'est présente pour aider Google à comprendre l'arborescence du site.

_Figure 4 : Aperçu actuel des Sitelinks sur Google._

**Analyse des Sitelinks actuels :** Bien que Google affiche des sous-liens (Sitelinks), leur sélection est automatique et non maîtrisée. On y trouve des pages pertinentes ("Police Municipale", "Uniformes") mais aussi des pages moins stratégiques ou mal décrites ("Explorez", "Tshirts - Polos" avec une description tronquée sur la newsletter).\
**Recommandation :**

* Envelopper le menu principal dans une balise `<nav role="navigation">`.
* Ajouter le balisage JSON-LD `SiteNavigationElement` pour lister explicitement les rubriques principales que vous souhaitez voir apparaître dans ces Sitelinks. Cela donne des indications fortes à Google sur les pages réellement importantes de votre arborescence.

## Optimisation des Ancres de Liens (Mots-clés du Menu)

**Constat :** Les intitulés du menu (sous-catégories) sont actuellement très génériques (ex: "Hauts", "Bas", "Tête - Coiffes", "Équipements"). Pour Google, le texte d'un lien (l'ancre) est un signal fort pour comprendre le contenu de la page de destination. Un lien "Hauts" n'a aucune valeur SEO.\
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

**Constat :** Les liens du menu pointent vers des URLs contenant des paramètres de filtres (ex: `/uniformes/hauts?univers=["Police+Municipale"]`).\
**Impact :** Les URLs avec paramètres sont moins bien comprises et indexées par Google que des URLs statiques et propres.\
**Recommandation :** Transformer ces liens paramétrés en véritables URLs "propres" (ex: `/police-municipale/uniformes/hauts`). Cela créera de véritables pages "catégories" optimisables pour le SEO.

