import requests
from bs4 import BeautifulSoup
import time

# On cible le top des jeux vidéo
url = "https://www.senscritique.com/jeuxvideo/tops/top111"

# Le "User-Agent" est obligatoire ici pour éviter d'être bloqué
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

print("Connexion à SensCritique...")
reponse = requests.get(url, headers=headers)

if reponse.status_code == 200:
    soup = BeautifulSoup(reponse.text, "html.parser")
    
    # Sur SensCritique, chaque jeu est dans un bloc 'ProductListItem'
    # On utilise un sélecteur partiel pour être plus flexible
    jeux = soup.find_all("div", attrs={"data-testid": "product-list-item"})
    
    print(f"\n✅ {len(jeux)} jeux trouvés sur cette page :")
    print("-" * 40)

    for i, jeu in enumerate(jeux[:15], 1): # On affiche les 15 premiers
        # Le titre est dans un lien avec l'attribut data-testid="product-title"
        balise_titre = jeu.find("a", attrs={"data-testid": "product-title"})
        # La note est souvent dans une balise avec "rating"
        balise_note = jeu.find("div", attrs={"data-testid": "rating-number"})
        
        if balise_titre:
            titre = balise_titre.get_text(strip=True)
            note = balise_note.get_text(strip=True) if balise_note else "N/A"
            
            print(f"{i}. {titre} (Note : {note}/10)")
            print("-" * 10)
            
else:
    print(f"Erreur de connexion : {reponse.status_code}")