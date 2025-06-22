# Projet Data Jobs – AWS ETL

## Objectif
Automatiser la récupération, le traitement et la visualisation d’offres d’emploi Data.

## Architecture
- API Pôle Emploi
- Pipeline ETL (Python)
- PostgreSQL (Amazon RDS)
- Stockage CSV (local et S3)
- Visualisation avec Dash et Bokeh

## Structure
- `etl/`: scripts d'extraction, transformation, chargement
- `data/`: outputs CSV
- `dashboard.py`: visualisation interactive

## Lancement du pipeline
```bash
python etl/etl_pipeline.py
