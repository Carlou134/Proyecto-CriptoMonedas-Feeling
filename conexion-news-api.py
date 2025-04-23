import requests
import pandas as pd

# Coloca tu clave real aquí
NEWSAPI_KEY = '7f38569b51184d29a8b6141a781c75b9'

def obtener_noticias(query="economy", lenguaje="es", maximo=10):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "language": lenguaje,
        "sortBy": "publishedAt",
        "pageSize": maximo,
        "apiKey": NEWSAPI_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(f"Error NewsAPI: {response.status_code} - {response.text}")
    noticias = response.json()["articles"]
    return pd.DataFrame(noticias)[["source", "title", "description", "publishedAt", "url"]]

temas = ["Ethereum ETF", "Bitcoin regulación", "DeFi tendencia"]
dfs = []

for tema in temas:
    df = obtener_noticias(query=tema, lenguaje="es", maximo=10)
    dfs.append(df)

# Unir todos en un solo DataFrame
df_total = pd.concat(dfs, ignore_index=True)
df_total.to_csv("noticias_combinadas.csv", index=False)
