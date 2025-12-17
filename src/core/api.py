# src/core/api.py

import requests
from config.settings import TIMEOUT


class APIClient:
    """Hybrid Analysis API ile HTTP haberleşmesini yapan katman"""

    BASE_URL = "https://hybrid-analysis.com/api/v2"

    def __init__(self, api_key : str, timeout=TIMEOUT):
        self.api_key = api_key
        if not api_key:
            raise ValueError("api_key is required")
        
        self.timeout = timeout
        self.headers = {
            "api-key": self.api_key,
            "User-Agent": "Falcon"
        }

    def get(self, path: str, params: dict | None = None) -> dict:
        url = f"{self.BASE_URL}{path}"

        response = requests.get(
            url,
            headers=self.headers,
            params=params,
            timeout=self.timeout
        )

        response.raise_for_status()
        return response.json()


    def post(self, path: str, data: dict | None = None, files: dict | None = None) -> dict:
        url = f"{self.BASE_URL}{path}"

        response = requests.post(
            url,
            headers=self.headers,
            data=data,
            files=files,
            timeout=self.timeout * 2
        )

        response.raise_for_status()
        return response.json()
