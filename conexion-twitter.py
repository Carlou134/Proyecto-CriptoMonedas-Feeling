import requests
import pandas as pd

# Reemplaza esto con tu Bearer Token
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAABU00wEAAAAAXW6W1duZIySgAy4xf%2FDshVP3%2Frs%3DYcvuwpjpgoYwVtLCTajyFEXV00QWgHUTvcLxJvhYWVasAzFMRl'

def crear_headers(token):
    return {"Authorization": f"Bearer {token}"}

def buscar_tweets(query, max_results=10):
    url = "https://api.twitter.com/2/tweets/search/recent"
    headers = crear_headers(BEARER_TOKEN)
    params = {
        "query": query,
        "tweet.fields": "created_at,author_id,text",
        "max_results": max_results
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(f"Error: {response.status_code} - {response.text}")
    return response.json()

# Ejemplo: buscar "dólar Perú"
resultados = buscar_tweets("(bitcoin OR ethereum OR altcoins OR solana) lang:es", max_results=50)

# Mostrar los resultados en DataFrame
df = pd.DataFrame(resultados["data"])
print(df.head())
df.to_csv("criptomonedas.csv", index=False)
