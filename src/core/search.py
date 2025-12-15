# src/core/search.py

from core.api import APIClient
from core.classifier import TargetClassifier, TargetType


class SearchService:
    """Hybrid Analysis üzerinde lookup (search) yapan servis"""

    def __init__(self, client: APIClient):
        self.client = client
        self.classifier = TargetClassifier()

    def detect_target_type(self, target: str) -> TargetType:
        """
        Target için otomatik tip tespiti yapar.
        SADECE --target yolunda kullanılmalıdır.
        """
        return self.classifier.classify(target)

    def search_by_filename(self, filename: str) -> dict:
        """
        Filename'e göre arama yapar.
        """
        return self.client.post(
            path="/search/terms",
            data={"filename": filename}
        )

    def search(self, target: str, target_type: TargetType) -> dict:
        """
        Belirtilmiş target_type'a göre arama yapar.
        """

        # UNKNOWN → kontrollü şekilde dur
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
        return self.client.post(
            path="/search/terms",
            data={target_type.value: target}
        )
