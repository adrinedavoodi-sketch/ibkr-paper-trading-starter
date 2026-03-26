from scanner import scan
from signals import should_buy, score_stock
from ibkr_client import IBKRClient
from config import ACCOUNT_ID, MIN_SCORE_TO_BUY

client = IBKRClient()

for row in scan():
    score = score_stock(row)
    if should_buy(row, MIN_SCORE_TO_BUY):
        print(f"BUY {row['symbol']} score={score}")
        # client.place_order(ACCOUNT_ID, row['symbol'], 'BUY', qty=1, order_type='LMT', limit_price=0)
    else:
        print(f"SKIP {row['symbol']} score={score}")
