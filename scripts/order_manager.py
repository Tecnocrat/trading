import logging
import requests

class OrderManager:
    def __init__(self):
        self.positions = {}  # Store active positions keyed by symbol

    def get_current_price(self, symbol):
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        response = requests.get(url)
        data = response.json()
        return float(data["price"])

    def open_position(self, symbol, amount, leverage, direction):
        current_price = self.get_current_price(symbol)
        position = {
            "symbol": symbol,
            "amount": amount,
            "leverage": leverage,
            "direction": direction,
            "entry_price": current_price,
            "entry_time": None  # Add timestamp here as needed
        }
        self.positions[symbol] = position
        logging.info(f"Opened {direction} position: {position}")
        return position

    def hedge_position(self, symbol, hedge_ratio):
        if symbol not in self.positions:
            logging.warning(f"No position found for {symbol} to hedge")
            return None

        pos = self.positions[symbol]
        hedge_amount = pos["amount"] * hedge_ratio
        logging.info(f"Hedging {symbol}: Opening counter position with amount {hedge_amount}")
        return hedge_amount
