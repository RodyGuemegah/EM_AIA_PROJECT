# 📊 Dashboard Plotly – Visualisation des Offres d'Emploi

Ce dashboard interactif a été conçu pour explorer les données d’offres d’emploi récupérées via l’API Pôle Emploi.

## 📁 Fichier source

- `etl/dashboard/dashboard.py`

## 📥 Données utilisées

- `etl/data/offres_data_scientist.csv`
  - Générées automatiquement par le pipeline ETL.
  - Contient les colonnes : `id`, `intitule`, `description`, `lieu`, `entreprise`, `dateCreation`, `salaire`, `contrat`.

## 🛠️ Technologies

- `pandas`
- `plotly`

## ⚙️ Installation des dépendances

```bash
pip install pandas plotly

##  ✅Lancement du dashboard

python etl/dashboard/dashboard.py
