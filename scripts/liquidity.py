from web3 import Web3
import json
import requests

# Load ABI from a JSON configuration file or string
with open("configs/pool_abi.json") as abi_file:
    POOL_ABI = json.load(abi_file)

class LiquidityPoolConnector:
    def __init__(self, rpc_url):
        self.web3 = Web3(Web3.HTTPProvider(rpc_url))
        if not self.web3.is_connected():
            raise ConnectionError("Failed to connect to BNB Chain RPC")
        print("Connected to BNB Chain")

    def is_connected(self):
        """Check if the connection to the blockchain is active."""
        return self.web3.is_connected()

    def get_pool_balance(self, token_address, pool_contract_address):
        """Fetch the balance of a token in a liquidity pool."""
        pool_contract = self.web3.eth.contract(address=pool_contract_address, abi=POOL_ABI)
        balance = pool_contract.functions.getBalance(token_address).call()
        return balance

    def execute_trade(self, pool_contract_address, trade_data, private_key):
        """Execute a trade on the liquidity pool."""
        pool_contract = self.web3.eth.contract(address=pool_contract_address, abi=POOL_ABI)
        transaction = pool_contract.functions.trade(trade_data).buildTransaction({
            'chainId': 56,  # BNB Chain chainId (56 for mainnet)
            'gas': 300000,
            'gasPrice': self.web3.toWei('5', 'gwei'),
            'nonce': self.web3.eth.getTransactionCount(self.web3.eth.account.privateKeyToAccount(private_key).address)
        })
        signed_tx = self.web3.eth.account.sign_transaction(transaction, private_key=private_key)
        tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(f"Trade executed, tx hash: {tx_hash.hex()}")
        return tx_hash

class BinanceAPI:
    @staticmethod
    def get_price(symbol="BNBUSDT"):
        """Fetch the current price of a cryptocurrency from Binance API."""
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return float(response.json()["price"])
        except (requests.RequestException, KeyError) as e:
            raise ValueError(f"Failed to fetch price for {symbol}: {e}")

if __name__ == "__main__":
    # Example usage of the refactored LiquidityPoolConnector and BinanceAPI
    bnb_rpc = "https://bsc-dataseed.binance.org/"
    connector = LiquidityPoolConnector(bnb_rpc)
    print("Connected to BNB:", connector.is_connected())

    # Fetch and print BNB price
    try:
        price = BinanceAPI.get_price()
        print("BNB Price:", price)
    except ValueError as e:
        print(e)
