import requests
from bs4 import BeautifulSoup
import csv
import time

url = "https://www.nintendo.com/fr-fr/Rechercher/Rechercher-299117.html?f=147394-5-10"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

print("Connexion au catalogue Nintendo...")
reponse = requests.get(url, headers=headers)

if reponse.status_code == 200:
    soup = BeautifulSoup(reponse.text, "html.parser")
    
    elements_jeux = soup.find_all("li", class_="page-list-group-item")
    
    print(f"\n {len(elements_jeux)} jeux trouvés. Sauvegarde en cours...")

    with open("jeux_nintendo.csv", "w", newline="", encoding="utf-8") as fichier:
        writer = csv.writer(fichier)
        writer.writerow(["titre", "prix", "console"])

        for jeu in elements_jeux[:15]:
            balise_titre = jeu.find(["h2", "h3", "h4", "p", "span"])
            balise_prix = jeu.find("span", class_="price")
            
            titre = balise_titre.get_text(strip=True) if balise_titre else "Titre introuvable"
            prix = balise_prix.get_text(strip=True) if balise_prix else "N/A"
            
            writer.writerow([titre, prix, "Nintendo Switch"])
                
        time.sleep(1)
        
    print("Scraping terminé ! Le fichier jeux_nintendo.csv est mis à jour.")
            
else:
    print(f"Erreur de connexion HTTP : {reponse.status_code}")