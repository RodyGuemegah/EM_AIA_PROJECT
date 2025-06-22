import requests
from requests.auth import HTTPBasicAuth

def get_token():
    client_id = "PAR_datalake_4fdfc597b8ed93677487a9b3d2aa86c3fad5d9ef69b57a7919cf70404fffbd73"
    client_secret = "849cd99480c68aa4927c62bcbb9c5d636681da94f4864591a3a7d07d430b2074"

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
