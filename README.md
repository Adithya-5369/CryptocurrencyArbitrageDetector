# Cryptocurrency Arbitrage Detector

## Overview

The **Cryptocurrency Arbitrage Detector** is a Python-based tool that helps identify potential arbitrage opportunities across different cryptocurrency exchanges. The tool fetches real-time cryptocurrency prices from multiple exchanges (Kraken, KuCoin, OKX, Coinbase, and CoinGecko) and compares them to detect price differences. If an arbitrage opportunity exists, it calculates and displays the potential profit percentage by buying from the lowest-priced exchange and selling at the highest-priced exchange.

## Features

- Fetch cryptocurrency prices from popular exchanges:
  - Kraken
  - KuCoin
  - OKX
  - Coinbase
  - CoinGecko
- Automatically detects price discrepancies between exchanges.
- Calculates and displays potential profit from arbitrage opportunities.
- Provides real-time price comparison from multiple sources.

## Requirements

Before running the tool, make sure you have Python 3.x installed along with the required libraries:

- `requests`: For making HTTP requests to the exchange APIs.

To install the required Python libraries, you can run:

```bash
pip install -r requirements.txt
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/CryptocurrencyArbitrageDetector.git
   cd CryptocurrencyArbitrageDetector
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the tool:

   ```bash
   python main.py
   ```

4. Input the cryptocurrency symbol (e.g., `BTCUSD`) when prompted.

## How It Works

- The script fetches live prices from Kraken, KuCoin, OKX, Coinbase, and CoinGecko.
- It compares prices and identifies the cheapest and most expensive exchange.
- If there is a price discrepancy (arbitrage opportunity), the script calculates the profit percentage and displays it.

## Example Output

```
Enter cryptocurrency symbol (e.g., BTCUSD): BTCUSD
Prices from exchanges:
Kraken: $30000.00
KuCoin: $29950.00
OKX: $30020.00
Coinbase: $30010.00
CoinGecko: $29990.00

Arbitrage Opportunity: Buy on KuCoin ($29950.00) and sell on OKX ($30020.00) for 0.23% profit.
```

## File Structure

```
CryptocurrencyArbitrageDetector/
│
├── main.py                     # Main script for detecting arbitrage opportunities
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

By: Adithya Sai Srinivas
