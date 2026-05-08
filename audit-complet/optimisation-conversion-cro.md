# Optimisation de la Conversion (CRO) - Page d'Accueil

## 6. Optimisation de la Conversion (CRO) - Page d'Accueil

### 🖼️ Hero Banner & Animation Commerciale (Calendrier Marketing)

**Constat :** Le "Hero Banner" (le grand visuel en haut de la page d'accueil) est la zone la plus visible du site. Actuellement, il ne semble pas exploité à son plein potentiel pour l'animation commerciale.\
**Recommandation :**

* **Promotions et Nouveautés :** Utiliser cet espace prioritairement pour mettre en avant les nouveautés produits et les offres promotionnelles en cours. Même dans une niche B2B/Institutionnelle, l'animation commerciale reste un levier de conversion majeur.
* **Planification Annuelle :** OROD dispose déjà d'une base de données de photographies de très haute qualité. Il serait extrêmement pertinent de planifier un **calendrier marketing annuel**.
* **Session de travail "Batching" :** Organiser une grande session de travail (design/marketing) pour créer d'un seul coup tous les visuels du Hero Banner et les bannières d'e-mailing correspondantes pour toute l'année (ex: Soldes d'hiver, Équipement d'été, Rentrée, Black Friday, etc.). Cela garantit une cohérence visuelle, un gain de temps énorme, et une animation continue du site sans effort au quotidien.
* **Automatisation sur-mesure (Mon accompagnement) :** Pour exécuter ce calendrier annuel sans friction, j'ai développé mes propres programmes sur-mesure. Une fois les visuels créés lors du batching, mes scripts se chargent de mettre à jour automatiquement les Hero Banners sur le site aux dates prévues, sans aucune intervention manuelle de votre part.

### 🤝 Preuve Sociale & Réassurance

**Constat :** Le site manque d'éléments de réassurance visibles sur la page d'accueil (avis clients, logos de partenaires, certifications, contact direct).\
**Recommandation :**

* **Logos Partenaires :** Ajouter un bandeau de logos des institutions ou collectivités qui font déjà confiance à OROD.
* **Avis Clients :** Intégrer un module d'avis (ex: Avis Vérifiés) pour rassurer sur la qualité des produits et du service.
* **Chiffres clés :** Mettre en avant des données rassurantes (ex: "Plus de 200 points de contact", "Livraison rapide").
* **Bloc "À votre écoute" :** Intégrer un bloc très visible avec les coordonnées de contact (téléphone, e-mail, horaires) pour humaniser la relation commerciale, particulièrement importante en B2B / institutionnel.

### 🧲 Capture de Leads (Pop-up & Widget)

**Constat :** La page d'accueil propose une simple ligne "Newsletter" en bas de page, ce qui génère un taux d'inscription très faible.\
**Recommandation :**

* **Pop-up au scroll ou à l'intention de sortie (Exit Intent) :** Déclencher une fenêtre pop-up proposant un avantage immédiat (ex: "10% de remise sur votre première commande" ou "Frais de port offerts") en échange de l'adresse e-mail.
* **Widget flottant :** Alternativement, un petit widget discret en bas à gauche de l'écran rappelant cette offre.
* **Impact chiffré (Benchmark E-commerce) :** Ce type de mécanique (Incentive vs E-mail) permet généralement de convertir jusqu'à **30% des visiteurs** en abonnés. Une fois l'e-mail capté, la conversion est beaucoup plus aisée via des séquences automatisées. Dans un e-commerce bien optimisé, le canal e-mail (Newsletters + Automations) doit représenter entre **20% et 30% du Chiffre d'Affaires global**. Bien que la niche institutionnelle d'OROD soit spécifique, la capture d'e-mails reste le levier d'acquisition le plus rentable.

### 🛍️ Affichage des Produits (Grilles & Survol)

**Constat 1 : Le nom de la marque.** Sous chaque titre de produit, le nom de la marque (ex: OROD, DMB) est affiché. Bien que pertinent dans un catalogue multi-marques, son affichage actuel manque de hiérarchie visuelle et ressemble à du texte brut.\
**Constat 2 : L'effet de survol (Hover) cassé.** Au repos, les vignettes produits sont bien carrées (ratio natif des images). Cependant, au survol de la souris sur une carte produit (page d'accueil ou catégorie), une seconde image s'affiche. Si cette seconde image est rectangulaire (horizontale ou verticale), elle "casse" la grille carrée, donnant un aspect non fini au site et déformant potentiellement l'image si elle est étirée.

**Recommandations :**

* **Pour le nom de la marque (SEO & UX) :** Améliorer la hiérarchie visuelle en plaçant la marque **au-dessus** du titre, sous forme de **badge cliquable** (ex: texte gris clair en majuscules). Ce lien redirigerait vers une page dédiée à la marque regroupant tous ses articles.
  * _Bénéfice SEO :_ Création de nouvelles pages d'atterrissage (Silos de marques) captant les requêtes spécifiques des utilisateurs qui cherchent un fabricant précis (ex: "Équipement DMB").
  * _Bénéfice CRO :_ Navigation facilitée pour les professionnels fidèles à une marque.
* **Affichage de la Catégorie (Maillage & Rétention) :** Ajouter le nom de la catégorie parente (ex: "Polos & T-shirts") sur la carte produit, idéalement sous forme de lien cliquable, juste à côté ou en dessous de la marque.
  * _Bénéfice SEO :_ Renforce massivement le maillage interne (liens) vers les pages catégories stratégiques et enrichit le champ lexical de la page d'accueil avec des mots-clés pertinents.
  * _Bénéfice CRO :_ Si le produit affiché ne plaît pas totalement, l'utilisateur peut facilement cliquer sur la catégorie pour voir les alternatives, le maintenant ainsi dans le tunnel d'achat (réduction du taux de rebond).
* **Pour le bug de l'image au survol :**
  * **Solution :** Les images secondaires (affichées au survol) sont déjà correctement configurées au format carré dans la base de données. Le problème vient d'un recadrage CSS ou d'un paramètre d'affichage qui force cette seconde image à devenir rectangulaire. Il suffit de **retirer ce recadrage forcé** dans le code (CSS ou configuration du thème) pour que la seconde image s'affiche dans son format carré natif, tout comme la première. Cela empêchera la grille de se casser sans nécessiter de retouche du catalogue.

