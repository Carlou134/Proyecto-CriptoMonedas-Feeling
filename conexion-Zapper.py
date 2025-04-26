import requests

# Reemplaza con tu API Key real
API_KEY = "31095ea1-5964-4c7a-8b46-13dd3d23df9b"
headers = {
    "Content-Type": "application/json",
    "x-zapper-api-key": API_KEY
}

query = """
query PortfolioV2($addresses: [Address!]!, $networks: [Network!]) {
  portfolioV2(addresses: $addresses, networks: $networks) {
    tokenBalances {
      byToken {
        edges {
          node {
            balance
            balanceUSD
            symbol
            name
          }
        }
      }
    }
  }
}
"""

variables = {
    "addresses": ["0x3d280fde2ddb59323c891cf30995e1862510342f"],
    "networks": ["ETHEREUM_MAINNET"]
}

response = requests.post(
    "https://public.zapper.xyz/graphql",
    json={"query": query, "variables": variables},
    headers=headers
)

data = response.json()
print(data)
