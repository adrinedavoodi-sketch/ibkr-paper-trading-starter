from scanner import scan
from signals import should_buy, score_stock
from ibkr_client import IBKRClient
from notifier import send_buy_alert, send_scan_summary
from config import ACCOUNT_ID, MIN_SCORE_TO_BUY

client = IBKRClient()
buy_signals = []
stocks = scan()

print("\n=== IBKR Paper Trading Scanner ===")
print(f"Minimum score to trigger BUY: {MIN_SCORE_TO_BUY}/4\n")

for row in stocks:
    score = score_stock(row)
    action = "BUY" if should_buy(row, MIN_SCORE_TO_BUY) else "SKIP"
    print(f"[{action}] {row['symbol']} | Score: {score}/4 | Price: ${row['price']} | Momentum: {row['momentum_pct']}%")

    if action == "BUY":
        buy_signals.append(row)
        send_buy_alert(
            symbol=row['symbol'],
            score=score,
            price=row['price'],
            momentum_pct=row['momentum_pct']
        )
        # Uncomment when ready for paper trades:
        # client.place_order(ACCOUNT_ID, row['symbol'], 'BUY', qty=1, order_type='LMT', limit_price=row['price'])

send_scan_summary(buy_signals, len(stocks))
print("\nScan complete.")
