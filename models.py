from typing import List
from pydantic import BaseModel


class Stock(BaseModel):
    year: str
    month: str

class StockList(BaseModel):
    stock: List[Stock]
