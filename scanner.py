WATCHLIST = ["AAPL", "MSFT", "NVDA", "AMZN", "META"]

def scan():
    return [{"symbol": s, "momentum": 1, "quality": 1, "valuation": 1} for s in WATCHLIST]
