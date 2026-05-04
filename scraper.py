import requests
from bs4 import BeautifulSoup
import csv  # 1. Ajout de la bibliothèque demandée[cite: 1]
import time

# On cible cette fois le top des films
url = "https://www.senscritique.com/films/tops/top111"

# Le "User-Agent" est obligatoire ici pour éviter d'être bloqué
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

print("Connexion à SensCritique (Section Films)...")
reponse = requests.get(url, headers=headers)

if reponse.status_code == 200:
    soup = BeautifulSoup(reponse.text, "html.parser")
    
    # Sur SensCritique, chaque film est dans un bloc 'ProductListItem'
    jeux = soup.find_all("div", attrs={"data-testid": "product-list-item"})
    
    print(f"\n✅ {len(jeux)} films trouvés sur cette page. Sauvegarde en cours...")
    print("-" * 40)

    # 2. Structure de la prof : On ouvre le fichier CSV en écriture[cite: 1]
    with open("top_films.csv", "w", newline="", encoding="utf-8") as fichier:
        writer = csv.writer(fichier)
        
        # On écrit l'en-tête du tableau[cite: 1]
        writer.writerow(["titre", "note"])

        for i, jeu in enumerate(jeux[:15], 1): # On affiche les 15 premiers
            # Le titre est dans un lien avec l'attribut data-testid="product-title"
            balise_titre = jeu.find("a", attrs={"data-testid": "product-title"})
            # La note est souvent dans une balise avec "rating"
            balise_note = jeu.find("div", attrs={"data-testid": "rating-number"})
            
            if balise_titre:
                titre = balise_titre.get_text(strip=True)
                note = balise_note.get_text(strip=True) if balise_note else "N/A"
                
                # Structure de la prof : On insère la ligne dans le CSV[cite: 1]
                writer.writerow([titre, note])
                
        # 3. Structure de la prof : Pause d'une seconde[cite: 1]
        time.sleep(1)
        
    print("Scraping terminé ! Le fichier top_films.csv a été créé.")
            
else:
    print(f"Erreur de connexion : {reponse.status_code}")