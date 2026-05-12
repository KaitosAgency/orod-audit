---
title: Optimisation de la Page d'Accueil (SEO & CRO)
description: "Refonte structurelle de la page d'accueil pour allier performance SEO et optimisation du taux de conversion (CRO)."
---

# Page d'Accueil

### Optimisation des Métadonnées (Title & Description)

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

**Constat sur la page d'accueil actuelle :**

* **Balise Title :** `<title>Orod - Uniformes, Décorations et Équipements Professionnels | OROD</title>`
* **Meta Description :** `<meta name="description" content="Uniformes, Équipements, Accessoires et Décorations pour les Armées, la Police Municipale, Gendarmerie, Pompiers...">`

**Analyse et Recommandations SEO :**

1. **Balise Title (Suroptimisée sur le nom de marque) :**
   * _Le problème :_ Le mot "Orod" ou "OROD" est répété deux fois, ce qui fait perdre de précieux caractères au profit d'autres mots-clés. La mention "Décorations" prend aussi de la place alors que le cœur de cible B2B cherche surtout du "matériel tactique" ou de "l'intervention".
   * _La solution :_ Épurer le titre pour cibler des mots-clés plus forts et plus transactionnels.
   * _Exemple recommandé :_ `<title>OROD | Équipements, Uniformes et Matériel Tactique pour Professionnels</title>`
2. **Meta Description (Manque d'Appel à l'Action) :**
   * _Le problème :_ La description actuelle est une simple liste de mots-clés qui se termine par des points de suspension `...` (probablement coupée ou mal rédigée). Elle n'incite pas vraiment au clic.
   * _La solution :_ Rédiger une phrase complète, accrocheuse, et terminer par un appel à l'action clair.
   * _Exemple recommandé :_ `<meta name="description" content="Découvrez le catalogue OROD : uniformes réglementaires, équipements tactiques et matériel d'intervention pour Police, Gendarmerie, Armées et Pompiers. Qualité et livraison rapide.">`

### Hiérarchie des titres (H1, H2, H3)

Le balisage actuel ne permet pas à Google de comprendre l'importance de vos contenus. Il y a actuellement deux titres "H1" (dont un sur un message administratif), ce qui est déconseillé.

**Nouvelle structure proposée :**

<table><thead><tr><th width="94">Niveau</th><th>Texte préconisé</th><th>Pourquoi ?</th></tr></thead><tbody><tr><td><strong>H1</strong></td><td><strong>OROD : Équipements, uniformes et matériel tactique pour les forces de sécurité</strong></td><td>Définit l'identité et le cœur de métier immédiatement pour Google et l'utilisateur.</td></tr><tr><td><strong>H2</strong></td><td><strong>Notre sélection d'équipements et uniformes professionnels</strong></td><td>Structure la première section de produits avec des mots-clés.</td></tr><tr><td><strong>H2</strong></td><td><strong>Gamme ORION : Vêtements tactiques et d'intervention</strong></td><td>Met en avant la marque propre en précisant la nature des produits.</td></tr><tr><td><strong>H2</strong></td><td><strong>Découvrez nos équipements par univers métiers</strong></td><td>Guide l'utilisateur vers les catégories clés (Police, Gendarmerie, etc.).</td></tr><tr><td><strong>H3</strong></td><td><strong>Paiement Chorus Pro pour les administrations</strong></td><td>Relègue l'info administrative au bon niveau tout en restant clair.</td></tr></tbody></table>

**Cartes produits (grilles accueil et catégories) :**

Encadrer chaque vignette dans une balise **`<article>`** (voir la page [Univers & Catégories](pages-univers-categories.md) pour le détail).

Utiliser une balise **`<h3>`** pour le titre de chaque produit dans la carte, sous les **`h2`** qui structurent les sections (« Notre sélection », « Gamme ORION », etc.).

Hiérarchie cible : **H1** page → **H2** section → **H3** titre produit.

Le rendu visuel (taille de police, graisse) reste libre via le CSS : seule la structure HTML compte pour le référencement.

### Rédactionnel & Maillage (Copywriting)

La page d'accueil est très visuelle mais manque de texte descriptif pour Google.

* **Introduction :** Ajouter 2 ou 3 lignes sous le titre principal pour expliquer qui est OROD et ce que vous proposez.
* **Mise en avant des catégories stratégiques :** Créer une section "Nos pôles d'expertise" présentant les catégories majeures avec un court texte descriptif.
  * **Proposition de contenu :**
    * **Police Municipale** : Uniformes, gilets pare-balles et équipements tactiques conformes aux décrets. Qualité et durabilité pour vos missions quotidiennes.
    * **Gendarmerie** : Équipements spécialisés, bagagerie tactique et tenues d'intervention robustes pour répondre aux exigences opérationnelles.
    * **Pompiers** : Vêtements de protection et équipements de secours pour les sapeurs-pompiers, alliant sécurité et ergonomie.
    * **Armées** : Matériel militaire et équipements de combat à haute technicité pour accompagner les forces armées dans toutes leurs missions.
  * **Bénéfice :** Cela permet d'injecter du vocabulaire métier spécifique dès la home et d'améliorer le maillage interne.
* **Appels à l'action (CTA) :** Remplacer les boutons "DÉCOUVREZ" par des textes plus incitatifs et précis comme _"Voir l'univers Police Municipale"_ ou _"Découvrir la gamme Orion"_.

### Hero Banner & Animation Commerciale (Calendrier Marketing)

**Constat :** Le "Hero Banner" (le grand visuel en haut de la page d'accueil) est la zone la plus visible du site. Actuellement, il ne semble pas exploité à son plein potentiel pour l'animation commerciale.

**Recommandation :**

* **Promotions et Nouveautés :** Utiliser cet espace prioritairement pour mettre en avant les nouveautés produits et les offres promotionnelles en cours. Même dans une niche B2B/Institutionnelle, l'animation commerciale reste un levier de conversion majeur.
* **Planification Annuelle :** OROD dispose déjà d'une base de données de photographies de très haute qualité. Il serait extrêmement pertinent de planifier un **calendrier marketing annuel**.
* **Session de travail "Batching" :** Organiser une grande session de travail (design/marketing) pour créer d'un seul coup tous les visuels du Hero Banner et les bannières d'e-mailing correspondantes pour toute l'année (ex: Soldes d'hiver, Équipement d'été, Rentrée, Black Friday, etc.). Cela garantit une cohérence visuelle, un gain de temps énorme, et une animation continue du site sans effort au quotidien.
* **Automatisation sur-mesure (Mon accompagnement) :** Pour exécuter ce calendrier annuel sans friction, j'ai développé mes propres programmes sur-mesure. Une fois les visuels créés lors du batching, mes scripts se chargent de mettre à jour automatiquement les Hero Banners sur le site aux dates prévues, sans aucune intervention manuelle de votre part.

### Preuve Sociale & Réassurance

**Constat :** Le site manque d'éléments de réassurance visibles sur la page d'accueil (avis clients, logos de partenaires, certifications, contact direct).

**Recommandation :**

* **Logos Partenaires :** Ajouter un bandeau de logos des institutions ou collectivités qui font déjà confiance à OROD.
* **Avis Clients :** Intégrer un module d'avis (ex: Avis Vérifiés) pour rassurer sur la qualité des produits et du service.
* **Chiffres clés :** Mettre en avant des données rassurantes (ex: "Plus de 200 points de contact", "Livraison rapide").
* **Bloc "À votre écoute" :** Intégrer un bloc très visible avec les coordonnées de contact (téléphone, e-mail, horaires) pour humaniser la relation commerciale, particulièrement importante en B2B / institutionnel.

### Capture de Leads (Pop-up & Widget)

**Constat :** La page d'accueil propose une simple ligne "Newsletter" en bas de page, ce qui génère un taux d'inscription très faible.

**Recommandation :**

* **Pop-up au scroll ou à l'intention de sortie (Exit Intent) :** Déclencher une fenêtre pop-up proposant un avantage immédiat (ex: "10% de remise sur votre première commande" ou "Frais de port offerts") en échange de l'adresse e-mail.
* **Widget flottant :** Alternativement, un petit widget discret en bas à gauche de l'écran rappelant cette offre.
* **Impact chiffré (Benchmark E-commerce) :** Ce type de mécanique (Incentive vs E-mail) permet généralement de convertir une part significative des visiteurs en abonnés (les benchmarks B2C citent souvent jusqu'à **~30%** dans des contextes très optimisés — à prendre comme ordre de grandeur, pas comme garantie). Une fois l'e-mail capté, la conversion est beaucoup plus aisée via des séquences automatisées. **En B2B / institutionnel**, la part du CA directement attribuable au canal e-mail est en pratique souvent plus modeste qu'en B2C grand public : viser **5 à 15%** du chiffre d'affaires via e-mail (newsletter + automatisations) peut être un objectif réaliste une fois le tunnel mature ; les **20 à 30%** restent un repère typique du **e-commerce B2C** bien rodé. Dans tous les cas, la capture d'e-mails reste un levier à fort ROI à ne pas négliger.

### Affichage des Produits (Grilles & Survol)

<figure><img src="../../.gitbook/assets/image (1) (2).png" alt=""><figcaption></figcaption></figure>

**Constat 1 : Le nom de la marque.** Sous chaque titre de produit, le nom de la marque (ex: OROD, DMB) est affiché. Bien que pertinent dans un catalogue multi-marques, son affichage actuel manque de hiérarchie visuelle et ressemble à du texte brut.

**Constat 2 : L'effet de survol (Hover) cassé.** Au repos, les vignettes produits sont bien carrées (ratio natif des images). Cependant, au survol de la souris sur une carte produit (page d'accueil ou catégorie), une seconde image s'affiche. Si cette seconde image est rectangulaire (horizontale ou verticale), elle "casse" la grille carrée, donnant un aspect non fini au site et déformant potentiellement l'image si elle est étirée.

**Recommandations :**

* **Pour le nom de la marque (SEO & UX) :** Améliorer la hiérarchie visuelle en plaçant la marque **au-dessus** du titre, sous forme de **badge cliquable** (ex: texte gris clair en majuscules). Ce lien redirigerait vers une page dédiée à la marque regroupant tous ses articles.
  * _Bénéfice SEO :_ Création de nouvelles pages d'atterrissage (Silos de marques) captant les requêtes spécifiques des utilisateurs qui cherchent un fabricant précis (ex: "Équipement DMB").
  * _Bénéfice CRO :_ Navigation facilitée pour les professionnels fidèles à une marque.
* **Affichage de la Catégorie (Maillage & Rétention) :** Ajouter le nom de la catégorie parente (ex: "Polos & T-shirts") sur la carte produit, idéalement sous forme de lien cliquable, en dessous du titre ou tout en haut de la carte (choix UX).
  * _Bénéfice SEO :_ Renforce massivement le maillage interne (liens) vers les pages catégories stratégiques et enrichit le champ lexical de la page d'accueil avec des mots-clés pertinents.
  * _Bénéfice CRO :_ Si le produit affiché ne plaît pas totalement, l'utilisateur peut facilement cliquer sur la catégorie pour voir les alternatives, le maintenant ainsi dans le tunnel d'achat (réduction du taux de rebond).
* **Pour le bug de l'image au survol :**
  * **Solution :** Les images secondaires (affichées au survol) sont déjà correctement configurées au format carré dans la base de données. Le problème vient d'un recadrage CSS ou d'un paramètre d'affichage qui force cette seconde image à devenir rectangulaire. Il suffit de **retirer ce recadrage forcé** dans le code (CSS ou configuration du thème) pour que la seconde image s'affiche dans son format carré natif, tout comme la première. Cela empêchera la grille de se casser sans nécessiter de retouche du catalogue.

### Données structurées complémentaires : `ItemList` via le module de Grille Produit

**Constat sur OROD :** Sur la page d’accueil, le JSON-LD (`@graph`) couvre surtout **`WebSite`**, **`WebPage`**, **`Organization`** et **`ImageObject`**. Il **n’inclut pas** de schéma **`ItemList`** décrivant les produits listés dans les grilles.

**Recommandation technique :** L'architecture de la page d'accueil (sous Odoo Shop Invaders / Vue.js) étant modulaire, ces données structurées ne doivent pas être codées "en dur" sur la page d'accueil. Il faut **intégrer la génération du JSON-LD `ItemList` directement au sein du composant/module de "Grille Produit" (Product Grid)**. Ainsi, chaque fois qu'une grille de produits est appelée (que ce soit sur la page d'accueil, sur une page catégorie, ou dans un article de blog), le module générera automatiquement le balisage `ItemList` correspondant avec une entrée par produit visible (nom + URL canonique, position). Cela garantit un référencement dynamique et parfait à l'échelle de tout le site, sans effort supplémentaire.
