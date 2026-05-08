# Page d'accueil

## Hiérarchie des titres (H1, H2, H3)

Le balisage actuel ne permet pas à Google de comprendre l'importance de vos contenus. Il y a actuellement deux titres "H1" (dont un sur un message administratif), ce qui est déconseillé.

**Nouvelle structure proposée :**

<table><thead><tr><th width="94">Niveau</th><th>Texte préconisé</th><th>Pourquoi ?</th></tr></thead><tbody><tr><td><strong>H1</strong></td><td><strong>OROD : Équipements, uniformes et matériel tactique pour les forces de sécurité</strong></td><td>Définit l'identité et le cœur de métier immédiatement pour Google et l'utilisateur.</td></tr><tr><td><strong>H2</strong></td><td><strong>Notre sélection d'équipements et uniformes professionnels</strong></td><td>Structure la première section de produits avec des mots-clés.</td></tr><tr><td><strong>H2</strong></td><td><strong>Gamme ORION : Vêtements tactiques et d'intervention</strong></td><td>Met en avant la marque propre en précisant la nature des produits.</td></tr><tr><td><strong>H2</strong></td><td><strong>Découvrez nos équipements par univers métiers</strong></td><td>Guide l'utilisateur vers les catégories clés (Police, Gendarmerie, etc.).</td></tr><tr><td><strong>H3</strong></td><td><strong>Paiement Chorus Pro pour les administrations</strong></td><td>Relègue l'info administrative au bon niveau tout en restant clair.</td></tr></tbody></table>

**Cartes produits (grilles accueil et catégories) :**

Encadrer chaque vignette dans une balise **`<article>`** (voir §3.3 pour le détail).

Utiliser une balise **`<h3>`** pour le titre de chaque produit dans la carte, sous les **`h2`** qui structurent les sections (« Notre sélection », « Gamme ORION », etc.).

Hiérarchie cible : **H1** page → **H2** section → **H3** titre produit.

Le rendu visuel (taille de police, graisse) reste libre via le CSS : seule la structure HTML compte pour le référencement.

## Rédactionnel & Maillage (Copywriting)

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

