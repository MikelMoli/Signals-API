import os

import psycopg2
import yaml

def get_connector():
    conn = psycopg2.connect(
                host="127.0.0.1", # name of container
                port="6000",
                database='financial_data',
                user='airflow',
                password='airflow'
            )

    return conn

def get_query(query_name):
    query = None
    with open(os.path.join('yaml/db_insert.yml'), 'r') as fp:
        query = yaml.safe_load(fp)[query_name]
    return query
