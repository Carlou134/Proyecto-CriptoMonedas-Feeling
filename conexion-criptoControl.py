import requests
import pandas as pd

# Tu API Key
CRYPTOCONTROL_API_KEY = 'TU_API_KEY'

# Función para obtener noticias de criptomonedas
def obtener_noticias_cryptocontrol():
    url = "https://cryptocontrol.io/api/v1/public/news"
    headers = {
        "x-api-key": CRYPTOCONTROL_API_KEY
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Error CryptoControl: {response.status_code} - {response.text}")
    noticias = response.json()
    return pd.DataFrame(noticias)[["title", "publishedAt", "url", "source"]]

# Ejemplo de uso
df_crypto_noticias = obtener_noticias_cryptocontrol()
print(df_crypto_noticias.head())
