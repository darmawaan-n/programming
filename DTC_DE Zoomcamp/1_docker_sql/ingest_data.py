import pandas as pd
import numpy as np
from time import time
from sqlalchemy import create_engine
import argparse as ap
import os

def main(params):
    username = params.username
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table = params.table
    # data_url = params.data_url

    # Import data to our dataframe
    data = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet"

    df = pd.read_parquet(data)

    # Generate chunked dataframe that consists of 20 pieces
    df_chunk = np.array_split(df, 20)

    # This will create an engine, an instant that can be used if we want to communicate with our database
    # The explanation is this:
    #     postgresql  = the name of RDBMS which we will use
    #     (1st) root  = username 
    #     (2nd) root  = password 
    #     localhost   = host in which our DB reside
    #     5432        = port of our DB
    #     ny_taxi     = the name of the DB Schema

    engine = create_engine(f"postgresql://{username}:{password}@{host}:{port}/{db}")

    # Let's create a loop where we can insert data by the size of its chunk
    for i in range(len(df_chunk)):
        t_start = time()

        df_chunk[i].to_sql(name=table, con=engine, if_exists="append")

        t_end = time()

        print(f"Successfully inserted another chunk! It took {(t_end - t_start):.4f} seconds...")

if __name__ == "__main__":
    parser = ap.ArgumentParser(description="Ingest data into PostgreSQL")

    parser.add_argument("--username", help='server username')
    parser.add_argument("--password", help='server password')
    parser.add_argument("--host", help='server host')
    parser.add_argument("--port", help='server port')
    parser.add_argument("--db", help='server database')
    parser.add_argument("--table", help='database table')
    # parser.add_argument("data_url", help='url of the data')

    args = parser.parse_args()

    main(args)