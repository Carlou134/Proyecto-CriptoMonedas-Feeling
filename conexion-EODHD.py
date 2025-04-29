import requests
import pandas as pd

# Tu API KEY
EODHD_API_KEY = '6810897b1933f5.11152765'

# Función para obtener noticias financieras
def obtener_noticias_eodhd(symbol="AAPL.US"):
    url = f"https://eodhd.com/api/news"
    params = {
        "api_token": EODHD_API_KEY,
        "s": symbol,
        "limit": 10,  # Número de noticias
        "fmt": "json"  # Formato de respuesta
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(f"Error EODHD: {response.status_code} - {response.text}")
    noticias = response.json()
    return pd.DataFrame(noticias)[["title", "content", "date", "link"]]

# Prueba
df_noticias_eodhd = obtener_noticias_eodhd("AAPL.US")
print(df_noticias_eodhd.head())
