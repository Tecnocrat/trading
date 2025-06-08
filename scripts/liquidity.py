from web3 import Web3
import json

# Load ABI from a JSON configuration file or string
with open("configs/pool_abi.json") as abi_file:
    POOL_ABI = json.load(abi_file)

class LiquidityPoolConnector:
    def __init__(self, rpc_url):
        self.web3 = Web3(Web3.HTTPProvider(rpc_url))
        if not self.web3.isConnected():
            raise Exception("Failed to connect to BNB Chain RPC")
        print("Connected to BNB Chain")

    def get_pool_balance(self, token_address, pool_contract_address):
        pool_contract = self.web3.eth.contract(address=pool_contract_address, abi=POOL_ABI)
        balance = pool_contract.functions.getBalance(token_address).call()
        return balance

    def execute_trade(self, pool_contract_address, trade_data, private_key):
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
