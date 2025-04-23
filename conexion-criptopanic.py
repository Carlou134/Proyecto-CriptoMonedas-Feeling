import requests
import pandas as pd

# Requiere también requests
CRYPTO_API_KEY = '301c8f740ef205a67a57947de46017b5c53b1e88'

def obtener_noticias_crypto(tipo="news", monedas="btc,eth", idioma="es"):
    url = "https://cryptopanic.com/api/v1/posts/"
    params = {
        "auth_token": CRYPTO_API_KEY,
        "currencies": monedas,
        "public": "true",
        "kind": tipo,
        "regions": "es",
        "filter": "important"
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(f"Error CryptoPanic: {response.status_code} - {response.text}")
    data = response.json()["results"]
    return pd.DataFrame(data)[["title", "published_at", "url", "votes"]]

# Ejemplo de uso
df_crypto = obtener_noticias_crypto(
    tipo="news",
    monedas="btc,eth,sol,ada,doge",
    idioma="es"
)
df_crypto.to_csv("criptopanic_completo.csv", index=False)

