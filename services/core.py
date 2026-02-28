import httpx
import os
from python_dotenv import load_dotenv

load_dotenv()

async def get_crypto_price(symbol: str):
    url = os.getenv("CRYPTO_API_URL")
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params={"symbol": symbol})
        return response.json()["price"]