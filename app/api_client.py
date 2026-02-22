import requests
from .config import API_URL

def generate_plan(note: str):
    response = requests.post(API_URL, params={"note": note})
    print("STATUS:", response.status_code)
    print("RAW BACKEND RESPONSE:", response.text)
    return response.json()["response"]