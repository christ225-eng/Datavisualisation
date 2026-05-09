import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.gog.com/fr/games?order=desc:sales"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

reponse = requests.get(url, headers=headers)

if reponse.status_code == 200:
    soup = BeautifulSoup(reponse.text, 'html.parser')
    jeux = soup.find_all("product-tile")
    
    nom_fichier = "data_gog.csv"
    
    with open(nom_fichier, "w", newline="", encoding="utf-8") as fichier:
        writer = csv.writer(fichier)
        writer.writerow(["Nom", "Prix", "Categorie", "Qualite_percue", "Source"])
        
        for jeu in jeux:
            titre = jeu.find("div", class_="product-tile__title")
            prix = jeu.find("span", class_="final-value")
            
            nom_jeu = titre.get_text(strip=True) if titre else "N/A"
            prix_jeu = prix.get_text(strip=True) if prix else "Gratuit"
            
            writer.writerow([nom_jeu, prix_jeu, "Meilleures ventes", "Très positif", "GOG"])
            
    print("Succès : Le fichier data_gog.csv a été créé.")
else:
    print("Erreur de connexion : " + str(reponse.status_code))