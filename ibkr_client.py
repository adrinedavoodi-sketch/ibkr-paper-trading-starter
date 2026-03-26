import requests
from config import IBKR_BASE_URL

class IBKRClient:
    def __init__(self, base_url=IBKR_BASE_URL):
        self.base_url = base_url.rstrip("/")

    def get_accounts(self):
        url = f"{self.base_url}/portfolio/accounts"
        return requests.get(url, verify=False, timeout=20).json()

    def place_order(self, account_id, conid, side, qty, order_type="LMT", limit_price=None):
        payload = {"conid": conid, "side": side, "quantity": qty, "orderType": order_type, "tif": "DAY"}
        if limit_price is not None:
            payload["price"] = limit_price
        url = f"{self.base_url}/iserver/account/{account_id}/orders"
        r = requests.post(url, json=payload, verify=False, timeout=20)
        r.raise_for_status()
        return r.json()
