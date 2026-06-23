import os
import requests
from dotenv import load_dotenv

load_dotenv()

INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
TOKEN = os.getenv("ZAPI_TOKEN")


def send_message(phone, message):
    url = (
        f"https://api.z-api.io/instances/{INSTANCE_ID}"
        f"/token/{TOKEN}/send-text"
    )

    payload = {
        "phone": phone,
        "message": message
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(
        url,
        json=payload,
        headers=headers,
        timeout=30
    )

    response.raise_for_status()

    return response.json()