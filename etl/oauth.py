import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os
def get_token():
    client_id = os.environ.get("POLE_EMPLOI_CLIENT_ID")
    client_secret = os.environ.get("POLE_EMPLOI_CLIENT_SECRET")
    auth_url = "https://entreprise.pole-emploi.fr/connexion/oauth2/access_token?realm=/partenaire"
    auth_data = {
        "grant_type": "client_credentials",
        "scope": "api_offresdemploiv2 o2dsoffre"
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(auth_url, data=auth_data, headers=headers, auth=HTTPBasicAuth(client_id, client_secret))
    response.raise_for_status()
    return response.json()["access_token"]
