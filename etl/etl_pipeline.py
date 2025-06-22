from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import save_csv, upload_to_s3, insert_to_postgres

def run_pipeline():
    print("📥 Extraction...")
    raw_data = extract_data()

    print("🔁 Transformation...")
    df = transform_data(raw_data)
    if df is None or df.empty:
        print("❌ La transformation a échoué ou le DataFrame est vide.")
        return

    print("💾 Sauvegarde CSV...")
    csv_path = save_csv(df)

    print("☁️ Upload S3...")
    upload_to_s3(csv_path, "data-lake-ds-rody", "offres_data_scientist.csv")

    print("🛢️ Insertion PostgreSQL...")
    insert_to_postgres(df)

    print("✅ Pipeline terminé avec succès !")
    
    print("📊 Aperçu des données transformées :")
    print(df.head())


if __name__ == "__main__":
    run_pipeline()
