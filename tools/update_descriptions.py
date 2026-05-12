import os
import re

descriptions = {
    "audit-complet/synthese.md": "Vue d'ensemble du plan d'action stratégique et des leviers d'acquisition pour transformer OROD en machine à conversion.",
    "audit-complet/ux-et-identite.md": "Analyse de l'interface, de la navigation et des éléments de réassurance pour maximiser la confiance et les conversions.",
    "audit-complet/anomalies-techniques.md": "Identification et correction des freins techniques majeurs (indexation, pagination, robots.txt) qui bloquent le référencement.",
    "audit-complet/strategie-seo/index.md": "Plan d'action global pour le référencement naturel, visant à dominer les résultats de recherche sur le secteur B2B/B2G.",
    "audit-complet/strategie-seo/menu-navigation.md": "Optimisation de l'arborescence et du maillage interne pour faciliter le parcours utilisateur et le crawl de Google.",
    "audit-complet/strategie-seo/page-accueil.md": "Refonte structurelle de la page d'accueil pour allier performance SEO et optimisation du taux de conversion (CRO).",
    "audit-complet/strategie-seo/pages-univers-categories.md": "Transformation des pages listes en véritables silos sémantiques pour capter le trafic qualifié sur des requêtes génériques.",
    "audit-complet/strategie-seo/fiches-produits.md": "Enrichissement des fiches produits avec des données structurées et du contenu expert pour maximiser les ventes.",
    "audit-complet/strategie-seo/elements-transverses.md": "Amélioration des signaux de confiance (E-E-A-T), du footer et des éléments globaux du site pour asseoir l'autorité de la marque.",
    "audit-complet/strategie-editoriale-et-blog.md": "Création d'une usine à contenu via un CMS Headless pour capter le trafic d'intention et nourrir l'autorité thématique.",
    "audit-complet/seo-programmatique-pseo.md": "Déploiement automatisé de milliers de pages ultra-ciblées (villes, métiers, normes) pour dominer la longue traîne.",
    "audit-complet/fidelisation-emailing.md": "Mise en place de scénarios de marketing automation pour maximiser la rétention et la valeur à vie (LTV) des clients.",
    "audit-complet/strategie-off-site.md": "Acquisition de backlinks de haute autorité pour booster la puissance du domaine (DR) et propulser les pages stratégiques.",
    "audit-complet/synergie-seo-sea.md": "Utilisation des campagnes Google Ads comme laboratoire de test pour accélérer et rentabiliser la stratégie SEO.",
    "audit-complet/geo.md": "Anticipation des moteurs de recherche génératifs (SGE, ChatGPT) en structurant les données pour l'Intelligence Artificielle.",
    "audit-complet/methodologie-mcp.md": "Explication du déploiement automatisé via l'agent IA et le protocole MCP connecté à l'ERP Odoo."
}

for filepath, desc in descriptions.items():
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if content.startswith('---'):
        end_idx = content.find('---', 3)
        if end_idx != -1:
            frontmatter = content[3:end_idx]
            rest = content[end_idx:]
            
            # Escape double quotes if any (though we don't have any here)
            safe_desc = desc.replace('"', '\\"')
            
            if 'description:' in frontmatter:
                new_frontmatter = re.sub(r'description:.*', f'description: "{safe_desc}"', frontmatter)
            else:
                new_frontmatter = frontmatter.rstrip() + f'\ndescription: "{safe_desc}"\n'
                
            new_content = '---' + new_frontmatter + rest
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
