import requests
import pandas as pd

# Tu API KEY
ALPHA_VANTAGE_API_KEY = '6810897b1933f5.11152765'

# Función para obtener datos de tiempo real de acciones
def obtener_datos_alpha(symbol="AAPL"):
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": "5min",
        "apikey": ALPHA_VANTAGE_API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(f"Error Alpha Vantage: {response.status_code} - {response.text}")
    datos = response.json()
    time_series = datos.get("Time Series (5min)", {})
    df = pd.DataFrame.from_dict(time_series, orient="index")
    df.reset_index(inplace=True)
    df.columns = ["timestamp", "open", "high", "low", "close", "volume"]
    return df

# Prueba
df_datos_alpha = obtener_datos_alpha("AAPL")
print(df_datos_alpha.head())
