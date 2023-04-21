import requests
import secrets

# Get user input for stock symbol
stock_symbol = input("Enter a stock symbol: ")

# Define the API endpoint and parameters
endpoint = f"https://api.polygon.io/v2/aggs/ticker/{stock_symbol}/prev"
params = {
    "apiKey": secrets.api_key,
    "adjusted": "true",
}

# Make the API request
response = requests.get(endpoint, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    last_price = data["results"][0]["c"]
    print(f"Last price for {stock_symbol}: ${last_price}")
else:
    print("Error: Unable to retrieve data")
