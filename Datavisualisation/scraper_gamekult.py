import requests
from bs4 import BeautifulSoup
import csv
import time

url = "https://www.gamekult.com"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

print("Connexion à Gamekult...")
reponse = requests.get(url, headers=headers)

if reponse.status_code == 200:
    soup = BeautifulSoup(reponse.text, "html.parser")
    articles = soup.find_all("article")
    
    print(f"\n✅ {len(articles)} articles trouvés. Sauvegarde en cours...")
    print("-" * 40)

    with open("actus_gamekult.csv", "w", newline="", encoding="utf-8") as fichier:
        writer = csv.writer(fichier)
        writer.writerow(["titre", "date_ou_categorie", "lien_article"])

        for article in articles[:15]: 
            # On élargit la recherche au cas où Gamekult utilise d'autres balises
            balise_titre = article.find(["h1", "h2", "h3", "h4", "p"])
            balise_meta = article.find(["time", "span"])
            balise_lien = article.find("a")
            
            # --- LA NOUVELLE LOGIQUE PLUS SOUPLE ---
            
            # Si on trouve le titre on le prend, sinon on écrit "Titre introuvable"
            titre = balise_titre.get_text(strip=True) if balise_titre else "Titre introuvable"
            
            # Pareil pour la date
            meta = balise_meta.get_text(strip=True) if balise_meta else "N/A"
            
            # Pareil pour le lien
            lien = "N/A"
            if balise_lien:
                lien = balise_lien.get("href", "N/A")
                if lien.startswith("/"):
                    lien = "https://www.gamekult.com" + lien
            
            # On enlève le "if" bloquant : on force l'écriture quoi qu'il arrive !
            writer.writerow([titre, meta, lien])
                
        time.sleep(1)
        
    print("Scraping terminé ! Le fichier actus_gamekult.csv est prêt.")
            
else:
    print(f"Erreur de connexion : {reponse.status_code}")