# Guide de Scraping - SensCritique
# TP Scraping - Analyse du Marché du Jeu Vidéo

Ce projet a pour objectif d'extraire des données provenant de différentes sources (médias, communautés et constructeurs) pour analyser l'écosystème du jeu vidéo, avec un focus sur **Sony** et ses concurrents.## 📋 Description des Scrapers

Le projet se compose de trois scripts de scraping distincts, développés en Python avec les bibliothèques `requests` et `BeautifulSoup` :1.  **SensCritique (`scraper.py`)** : Extrait le Top des films/jeux pour analyser la réception du public.[cite: 2]2.  **Gamekult (`scraper_gamekult.py`)** : Récupère les dernières actualités pour suivre les tendances médiatiques.[cite: 3]
3.  **Nintendo (`scraper_nintendo.py`)** : Scrape le catalogue d'un concurrent direct de Sony pour comparer les offres et les prix.[cite: 4]## 📊 Données Extraites

Chaque script génère un fichier CSV structuré pour l'analyse de données :- `top_films.csv` : Titres et notes de la communauté.[cite: 2]- `actus_gamekult.csv` : Titres, catégories et liens des articles de presse.[cite: 3]- `jeux_nintendo.csv` : Titres, prix et plateformes du catalogue concurrent.[cite: 4]## 🛠️ Installation et Utilisation### Prérequis- Python 3.x- Bibliothèques nécessaires : 
  ```bash
  pip install requests beautifulsoup4
  
Lancement
Pour exécuter les scrapers, utilisez les commandes suivantes dans le terminal :

Bash

python scraper.py
python scraper_gamekult.py
python scraper_nintendo.py