# src/core/parser.py

from core.api import APIClient


class SandboxParser:
    """
    Sandbox analiz sonuçlarını parse eden katman.
    """

    def __init__(self, client: APIClient):
        self.client = client

    def parse(self, job_id: str) -> dict:
        """
        Sandbox analiz sonucunu alır ve döner.
        """

        summary = self.client.get(
            path=f"/report/{job_id}/summary"
        )

        # TODO daha sonra istediğimiz şekilde parse etmek için buraya ilgili kod yazılacak 

        return {
            "summary": summary
        }


class QuickScanParser:
    """
    Quick Scan sonuçlarını parse eden katman.
    """
    
    def parse(self, response: dict) -> dict:
        return response

    # TODO daha sonra istediğimiz şekilde parse edeceğiz şimidlik olduğu gibi basılıyor