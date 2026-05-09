import requests
from bs4 import BeautifulSoup
import csv

url = "https://store.steampowered.com/search/?filter=topsellers"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

reponse = requests.get(url, headers=headers)

if reponse.status_code == 200:
    soup = BeautifulSoup(reponse.text, 'html.parser')
    jeux = soup.find_all("a", class_="search_result_row")
    
    nom_fichier = "data_monitor_export.csv"
    
    with open(nom_fichier, "w", newline="", encoding="utf-8") as fichier:
        writer = csv.writer(fichier)
        writer.writerow(["Nom", "Prix", "Categorie", "Qualite_percue", "Source"])

        for jeu in jeux:
            balise_titre = jeu.find("span", class_="title")
            balise_prix_promo = jeu.find("div", class_="discount_final_price")
            balise_prix_normal = jeu.find("div", class_="search_price")
            balise_avis = jeu.find("span", class_="search_review_summary")

            titre = balise_titre.get_text(strip=True) if balise_titre else "N/A"
            
            if balise_prix_promo:
                prix = balise_prix_promo.get_text(strip=True)
            elif balise_prix_normal:
                prix = balise_prix_normal.get_text(strip=True)
            else:
                prix = "N/A"
            
            avis = balise_avis.get("data-tooltip-html") if balise_avis else "Pas d'avis"
            avis = avis.replace("<br>", " - ")

            writer.writerow([titre, prix, "Meilleures ventes", avis, "Steam"])