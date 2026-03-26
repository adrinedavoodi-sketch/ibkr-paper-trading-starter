import yfinance as yf
import pandas as pd

WATCHLIST = ["AAPL", "MSFT", "NVDA", "AMZN", "META"]

def get_stock_data(symbol):
    ticker = yf.Ticker(symbol)
    info = ticker.info
    hist = ticker.history(period="3mo")

    if hist.empty:
        return None

    current_price = hist["Close"].iloc[-1]
    price_3mo_ago = hist["Close"].iloc[0]
    momentum = (current_price - price_3mo_ago) / price_3mo_ago  # % change over 3 months

    pe_ratio = info.get("trailingPE", None)
    profit_margin = info.get("profitMargins", None)
    debt_to_equity = info.get("debtToEquity", None)

    return {
        "symbol": symbol,
        "price": round(current_price, 2),
        "momentum_pct": round(momentum * 100, 2),
        "pe_ratio": pe_ratio,
        "profit_margin": profit_margin,
        "debt_to_equity": debt_to_equity,
    }

def scan():
    results = []
    for symbol in WATCHLIST:
        data = get_stock_data(symbol)
        if data:
            results.append(data)
            print(f"{symbol}: ${data['price']} | Momentum: {data['momentum_pct']}% | P/E: {data['pe_ratio']}")
    return results
