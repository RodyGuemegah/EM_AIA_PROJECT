from sqlalchemy import create_engine

import boto3
from sqlalchemy import create_engine
import os

def save_csv(df, path="data/offres_data_scientist.csv"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8")
    return path

def upload_to_s3(local_file, bucket_name, s3_key):
    s3 = boto3.client("s3")
    s3.upload_file(local_file, bucket_name, s3_key)

def insert_to_postgres(df):
    engine = create_engine("postgresql+psycopg2://postgres:Rodney0307@database-1.cz6ei0yka8yz.eu-west-3.rds.amazonaws.com:5432/postgres")
    df.to_sql("offres_data", engine, index=False, if_exists="replace")
