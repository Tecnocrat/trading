import plotly.graph_objects as go

def plot_trading_chart(price_data, positions):
    """
    price_data should be a dict with keys: 'time', 'open', 'high', 'low', 'close'
    positions is a dict of active positions.
    """
    fig = go.Figure(data=[go.Candlestick(
        x=price_data["time"],
        open=price_data["open"],
        high=price_data["high"],
        low=price_data["low"],
        close=price_data["close"],
        name="Market Price")])
    
    # Add position markers
    for pos in positions.values():
        fig.add_shape(
            type="line",
            x0=pos.get("entry_time"),
            y0=pos.get("entry_price"),
            x1=pos.get("entry_time"),
            y1=pos.get("entry_price"),
            line=dict(color="RoyalBlue", width=2),
            name=f"Position @ {pos.get('entry_price')}"
        )
    
    fig.update_layout(
        title="TradingChart with Active Positions",
        xaxis_title="Time",
        yaxis_title="Price"
    )
    fig.show()
