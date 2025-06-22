import requests
import pandas as pd
from etl.oauth import get_token  
from dotenv import load_dotenv

def extract_data():
    load_dotenv(".env")
    token = get_token()
    print("Voici le token reçu :")
    print(token[:50], "...")
    search_url = "https://api.pole-emploi.io/partenaire/offresdemploi/v2/offres/search"
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "motsCles": "data scientist",
        "range": "0-9",
        "departement": "75"
    }

    response = requests.get(search_url, headers=headers, params=params)

    if response.status_code in [200, 206]:
        return response.json()
    else:
        print("❌ Erreur lors de l'extraction :", response.text)
        return None
