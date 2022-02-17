from fastapi import FastAPI, Request
import uvicorn

import psycopg2
from psycopg2 import sql
import psycopg2.extras
from utils import get_connector, get_query

import pandas as pd
import yaml

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/stock")
def get_stock(data):
    return {"Hello": "World"}


@app.post("/stock")
async def add_stock(request: Request):
    request = await request.json()
    data = pd.json_normalize(request['data'])
    result = _insert_stock_data(data)
    # TODO:// Add try catch to handle failures and return a code or text with the response
    if result:
        response = {"Response": "OK"}
    else: 
        response = {"Response": "FAIL"}
    return response


def _insert_stock_data(data):
    result = False
    conn = None
    try:
        conn = get_connector()
        query = get_query('insert_stock_data')

        with conn.cursor() as cur:
            psycopg2.extras.execute_batch(cur=cur, sql=query, 
                                            argslist=data.to_dict(orient='records'))
            conn.commit()
        conn.commit()
        result = True
    finally:
        if conn is not None:
            conn.close()

    return result


#if __name__ == '__main__':
#    uvicorn.run(app, host='127.0.0.1', port=8000, debug=True)