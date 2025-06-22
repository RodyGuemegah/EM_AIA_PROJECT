import pandas as pd

def transform_data(raw_data):
    resultats = raw_data.get("resultats", [])
    if not resultats:
        print("⚠️ Aucun résultat trouvé.")
        return pd.DataFrame()  # Retourner un DataFrame vide au lieu de None

    data = []
    for offre in resultats:
        data.append({
            "id": offre.get("id"),
            "intitule": offre.get("intitule"),
            "description": offre.get("description"),
            "lieu": offre.get("lieuTravail", {}).get("libelle"),
            "entreprise": offre.get("entreprise", {}).get("nom"),
            "dateCreation": offre.get("dateCreation"),
            "salaire": offre.get("salaire", {}).get("libelle"),
            "contrat": offre.get("typeContratLibelle")
        })

    return pd.DataFrame(data)
