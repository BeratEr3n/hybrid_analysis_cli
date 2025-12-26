# src/core/parser.py

from core.api import APIClient
import json

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

        parsed = {
            "job_id": job_id,
            "status": summary.get("status"),
            "environment": summary.get("environment") or summary.get("environment_id"),
            "verdict": summary.get("verdict"),
            "threat_score": summary.get("threat_score") or summary.get("score"),
            "threat_level": summary.get("threat_level") or summary.get("level"),
            "totals": {
                "network_connections": summary.get("total_network_connections"),
                "processes": summary.get("total_processes"),
                "signatures": summary.get("total_signatures"),
            },
            "domains": summary.get("domains"),
            "started_at": summary.get("started_at") or summary.get("start_time"),
            "finished_at": summary.get("finished_at") or summary.get("end_time"),
        }

        json_output = json.dumps(parsed, indent=2, ensure_ascii=False)

        return json_output   



class QuickScanParser:
    """
    Quick Scan sonuçlarını parse eden katman.
    """
    
    def parse(self, response: dict) -> dict:
        
        scanners_v2 = response.get("scanners_v2", {})

        cleaned_scanners = {}

        for key, scanner in scanners_v2.items():
            if not scanner:
                cleaned_scanners[key] = None
                continue

            # shallow copy
            cleaned = dict(scanner)

            # uzun ve gürültülü alanı at
            cleaned.pop("reports", None)

            cleaned_scanners[key] = cleaned

        parsed = {
            "id": response.get("id"),
            "sha256": response.get("sha256"),
            "scanners_v2": cleaned_scanners,
            "finished": response.get("finished"),
        }

        json_output = json.dumps(parsed, indent=2, ensure_ascii=False)

        return json_output   


class SearchParser:
    """
    Search sonuçlarını parse eden katman.
    """

    def parse(self, search_result):
        parsed = search_result

        json_output = json.dumps(parsed, indent=2, ensure_ascii=False)

        return json_output
