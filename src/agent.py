import os
import requests
from dotenv import load_dotenv

load_dotenv()
print("🔑 API_KEY:", os.getenv("TRADING_SIM_API_KEY"))

API_KEY = os.getenv("TRADING_SIM_API_KEY")
API_URL = os.getenv("TRADING_SIM_API_URL", "https://api.competitions.recall.network")
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

class MCPClient:
    def __init__(self):
        self.base = API_URL

    def get_competition_status(self):
        resp = requests.get(f"{self.base}/api/competition/status", headers=HEADERS)
        resp.raise_for_status()
        return resp.json()

    def get_quote(self, from_token: str, to_token: str, amount: float):
        data = {"fromToken": from_token, "toToken": to_token, "amount": str(amount)}
        resp = requests.post(f"{self.base}/api/quote", headers=HEADERS, json=data)
        resp.raise_for_status()
        return resp.json()

    def execute_trade(self, from_token: str, to_token: str, amount: float, reasoning: str = ""):
        data = {
            "fromToken": from_token,
            "toToken": to_token,
            "amount": str(amount),
            "reason": reasoning
        }
        resp = requests.post(f"{self.base}/api/trade/execute", headers=HEADERS, json=data)
        resp.raise_for_status()
        return resp.json()
