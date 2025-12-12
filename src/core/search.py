# src/core/search.py

from core.api import APIClient
from core.classifier import TargetClassifier, TargetType


class SearchService:
    """Hybrid Analysis üzerinde lookup (search) yapan servis"""

    def __init__(self, client: APIClient, classifier: TargetClassifier):
        self.client = client
        self.classifier = classifier

    def search(self, target: str) -> dict:
        target_type = self.classifier.classify(target)

        # UNKNOWN → kontrollü dur
        if target_type == TargetType.UNKNOWN:
            return {
                "status": "unsupported_target",
                "target": target
            }

        # HASH → özel endpoint (GET)
        if target_type == TargetType.HASH:
            return self.client.get(
                path="/search/hash",
                params={"hash": target}
            )

        # IP / DOMAIN / URL → search/terms (POST)
        payload = {
            target_type.value: target
        }

        return self.client.post(
            path="/search/terms",
            data=payload
        )
