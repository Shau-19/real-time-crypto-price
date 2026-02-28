from pydantic import BaseModel

class CryptoPrice(BaseModel):
    symbol: str
    price: float