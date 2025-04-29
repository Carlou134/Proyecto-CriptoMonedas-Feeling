import requests
import pandas as pd

# Función para obtener precios actuales de criptomonedas
def obtener_precios_coingecko(moneda="bitcoin"):
    url = f"https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",        # Moneda de comparación
        "ids": moneda,               # ID de la criptomoneda
        "order": "market_cap_desc",
        "per_page": 1,
        "page": 1,
        "sparkline": False
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(f"Error CoinGecko: {response.status_code} - {response.text}")
    datos = response.json()
    return pd.DataFrame(datos)[["id", "symbol", "current_price", "market_cap", "total_volume", "price_change_percentage_24h"]]

# Ejemplo de uso
df_coingecko = obtener_precios_coingecko("bitcoin")
print(df_coingecko.head())
