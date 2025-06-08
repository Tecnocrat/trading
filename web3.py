from web3 import Web3
import requests

class BNBChainConnector:
    def __init__(self, rpc_url):
        self.web3 = Web3(Web3.HTTPProvider(rpc_url))
        if not self.web3.is_connected():
            raise ConnectionError("Failed to connect to BNB Chain RPC")

    def is_connected(self):
        return self.web3.is_connected()

class BinanceAPI:
    @staticmethod
    def get_price(symbol="BNBUSDT"):
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return float(response.json()["price"])
        except (requests.RequestException, KeyError) as e:
            raise ValueError(f"Failed to fetch price for {symbol}: {e}")

if __name__ == "__main__":
    # Connect to BNB Chain
    bnb_rpc = "https://bsc-dataseed.binance.org/"
    connector = BNBChainConnector(bnb_rpc)
    print("Connected to BNB:", connector.is_connected())

    # Fetch and print BNB price
    try:
        price = BinanceAPI.get_price()
        print("BNB Price:", price)
    except ValueError as e:
        print(e)
