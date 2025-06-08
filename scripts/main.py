import os
print("🔗 RPC URL:", os.getenv("BSC_RPC_URL"))
print("✅ Dependencies OK – ready to trade!")

import logging
from liquidity import LiquidityPoolConnector
from order_manager import OrderManager
from charting import plot_trading_chart

# Configure basic logging
logging.basicConfig(level=logging.INFO)

# Set RPC endpoint and private key (load safely from configs or environment variables)
RPC_URL = "https://bsc-dataseed.binance.org/"
PRIVATE_KEY = "YOUR_PRIVATE_KEY"  # caution: handle securely!

def main():
    # Initialize connectors and managers
    liquidity_connector = LiquidityPoolConnector(RPC_URL)
    order_manager = OrderManager()
    
    # Example: Open a leveraged long position on BNBUSDT
    symbol = "BNBUSDT"
    position = order_manager.open_position(symbol=symbol, amount=1.0, leverage=100, direction="LONG")
    
    # Fetch liquidity pool balance (example usage)
    pool_contract_address = "0xYourPoolContractAddress"
    token_address = "0xYourTokenAddress"
    balance = liquidity_connector.get_pool_balance(token_address, pool_contract_address)
    logging.info(f"Liquidity pool balance for token {token_address}: {balance}")
    
    # Dummy price data for charting; replace with actual historical data fetching
    price_data = {
        "time": ["2025-06-08 09:00", "2025-06-08 09:05", "2025-06-08 09:10"],
        "open": [300, 305, 310],
        "high": [310, 315, 320],
        "low": [295, 300, 305],
        "close": [305, 310, 315]
    }
    
    # Plot trading chart with the new position marked
    plot_trading_chart(price_data, order_manager.positions)
    
    # Add further trading logic and blockchain interactions as needed.
    # For example: liquidity_connector.execute_trade(pool_contract_address, trade_data, PRIVATE_KEY)

if __name__ == "__main__":
    main()
