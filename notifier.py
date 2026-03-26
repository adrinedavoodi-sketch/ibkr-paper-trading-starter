import os
import requests

SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")

def send_buy_alert(symbol, score, price, momentum_pct):
    if not SLACK_WEBHOOK_URL:
        print("[notifier] SLACK_WEBHOOK_URL not set, skipping alert.")
        return

    message = (
        f":green_circle: *BUY SIGNAL: {symbol}*\n"
        f"> *Price:* ${price}\n"
        f"> *Score:* {score}/4\n"
        f"> *3-Month Momentum:* {momentum_pct}%\n"
        f"> _Review in IBKR paper trading before placing any real orders._"
    )

    payload = {"text": message}
    response = requests.post(SLACK_WEBHOOK_URL, json=payload, timeout=10)
    if response.status_code == 200:
        print(f"[notifier] Slack alert sent for {symbol}")
    else:
        print(f"[notifier] Slack error {response.status_code}: {response.text}")

def send_scan_summary(buy_signals, total):
    if not SLACK_WEBHOOK_URL:
        return

    if not buy_signals:
        message = f":white_circle: *Scan complete* — No BUY signals today ({total} stocks scanned)."
    else:
        symbols = ", ".join([r['symbol'] for r in buy_signals])
        message = (
            f":bar_chart: *Scan Summary* — {len(buy_signals)}/{total} stocks triggered BUY\n"
            f"> *Signals:* {symbols}"
        )

    requests.post(SLACK_WEBHOOK_URL, json={"text": message}, timeout=10)
