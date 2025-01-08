import requests

# Fetch Prices from Kraken
def fetch_kraken_price(symbol):
    # Map standard symbols to Kraken's naming convention
    kraken_symbols = {"BTCUSD": "XXBTZUSD", "ETHUSD": "XETHZUSD"}  # Add more mappings as needed
    kraken_symbol = kraken_symbols.get(symbol, symbol)  # Default to input symbol if no mapping exists

    url = f"https://api.kraken.com/0/public/Ticker?pair={kraken_symbol}"
    response = requests.get(url)
    data = response.json()

    if "result" in data:
        for key in data["result"]:
            return float(data["result"][key]["c"][0])  # Current price
    else:
        print(f"Error: Kraken API did not return price for {symbol}. Response: {data}")
        return None

# Fetch Prices from KuCoin
def fetch_kucoin_price(symbol):
    kucoin_symbol = symbol.replace("USD", "-USDT")  # Convert to KuCoin format
    url = f"https://api.kucoin.com/api/v1/market/orderbook/level1?symbol={kucoin_symbol}"
    response = requests.get(url)
    data = response.json()

    if data.get("code") == "200000" and "data" in data and "price" in data["data"]:
        return float(data["data"]["price"])
    else:
        print(f"Error: KuCoin API did not return price for {kucoin_symbol}. Response: {data}")
        return None

# Fetch Prices from OKX
def fetch_okx_price(symbol):
    okx_symbol = symbol.replace("USD", "-USD")  # Convert to OKX format
    url = f"https://www.okx.com/api/v5/market/ticker?instId={okx_symbol}"
    response = requests.get(url)
    data = response.json()

    if data.get("code") == "0" and "data" in data and data["data"]:
        return float(data["data"][0]["last"])
    else:
        print(f"Error: OKX API did not return price for {okx_symbol}. Response: {data}")
        return None

# Fetch Prices from Coinbase
def fetch_coinbase_price(symbol):
    coinbase_symbol = symbol.replace("USD", "-USD")  # Convert to Coinbase format
    url = f"https://api.coinbase.com/v2/prices/{coinbase_symbol}/spot"
    response = requests.get(url)
    data = response.json()

    if "data" in data and "amount" in data["data"]:
        return float(data["data"]["amount"])
    else:
        print(f"Error: Coinbase API did not return price for {coinbase_symbol}. Response: {data}")
        return None

# Fetch Prices from CoinGecko
def fetch_coingecko_price(symbol):
    coingecko_symbols = {"BTCUSD": "bitcoin", "ETHUSD": "ethereum"}  # Add more mappings as needed
    coingecko_symbol = coingecko_symbols.get(symbol, symbol)  # Default to input symbol if no mapping exists

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coingecko_symbol}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()

    if coingecko_symbol in data and "usd" in data[coingecko_symbol]:
        return float(data[coingecko_symbol]["usd"])
    else:
        print(f"Error: CoinGecko API did not return price for {symbol}. Response: {data}")
        return None

# Detect Arbitrage Opportunities
def detect_arbitrage(symbol):
    kraken_price = fetch_kraken_price(symbol)
    kucoin_price = fetch_kucoin_price(symbol)
    okx_price = fetch_okx_price(symbol)
    coinbase_price = fetch_coinbase_price(symbol)
    coingecko_price = fetch_coingecko_price(symbol)

    prices = [
        ("Kraken", kraken_price),
        ("KuCoin", kucoin_price),
        ("OKX", okx_price),
        ("Coinbase", coinbase_price),
        ("CoinGecko", coingecko_price)
    ]

    # Filter out None values
    prices = [(exchange, price) for exchange, price in prices if price is not None]

    if len(prices) < 2:
        print("Not enough valid prices to detect arbitrage.")
        return

    # Display all prices
    print("Prices from exchanges:")
    for exchange, price in prices:
        print(f"{exchange}: ${price:.2f}")

    # Find arbitrage opportunities
    prices.sort(key=lambda x: x[1])  # Sort by price
    cheapest_exchange, cheapest_price = prices[0]
    most_expensive_exchange, most_expensive_price = prices[-1]

    profit_percentage = ((most_expensive_price - cheapest_price) / cheapest_price) * 100

    if profit_percentage > 0:
        print(f"Arbitrage Opportunity: Buy on {cheapest_exchange} (${cheapest_price:.2f}) and sell on {most_expensive_exchange} (${most_expensive_price:.2f}) for {profit_percentage:.2f}% profit.")
    else:
        print("No arbitrage opportunity found.")

# Main Execution
if __name__ == "__main__":
    symbol = input("Enter cryptocurrency symbol (e.g., BTCUSD): ").upper()
    detect_arbitrage(symbol)