import base64

import requests

from cf.backend.endpoints.core import BASE_URL

def verify(token: str):
    endpoint = f"{BASE_URL}/user/tokens/verify"
    headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
    resp = requests.get(
        endpoint,
        headers=headers
    ).json()
    return resp