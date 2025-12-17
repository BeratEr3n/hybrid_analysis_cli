# src/core/orchestration.py

from core.api import APIClient
from core.submission import SandboxSubmissionService
from core.poller import SandboxPoller
from core.parser import SandboxParser
from core.submission import QuickScanService
from core.poller import QuickScanPoller
from core.parser import QuickScanParser
from core.search import SearchService
from core.classifier import TargetType

class SandboxOrchestrator:
    """
    Sandbox analiz akışını uçtan uca yöneten orchestration katmanı.
    """

    def __init__(self, client: APIClient):
        self.client = client
        self.submission = SandboxSubmissionService(client)
        self.poller = SandboxPoller(client)
        self.parser = SandboxParser(client)

    def run_file(
        self,
        file_path: str,
        environment_id: int,
    ) -> dict:
        """
        Dosya için sandbox analiz akışını çalıştırır.
        """

        # 1. Submit
        submit_resp = self.submission.submit_file(
            file_path=file_path,
            environment_id=environment_id
        )

        job_id = submit_resp.get("job_id")
        if not job_id:
            raise RuntimeError("Sandbox submission did not return job_id")

        # 2. Poll
        state = self.poller.wait(job_id)

        # 3. Decision
        if state == "SUCCESS":
            return self.parser.parse(job_id=job_id)

        if state == "ERROR":
            return {
                "status": "ERROR",
                "job_id": job_id,
                "message": "Sandbox analysis failed"
            }

        # teorik olarak buraya düşmemeli
        return {
            "status": "UNKNOWN",
            "job_id": job_id,
            "message": f"Unexpected sandbox state: {state}"
        }


    def run_url(
        self,
        url: str,
        environment_id: int,
    ) -> dict:
        """
        URL için sandbox analiz akışını çalıştırır.
        """

        # 1. Submit
        submit_resp = self.submission.submit_url(
            url=url,
            environment_id=environment_id
        )

        job_id = submit_resp.get("job_id")
        if not job_id:
            raise RuntimeError("Sandbox submission did not return job_id")

        # 2. Poll
        state = self.poller.wait(job_id)

        # 3. Decision
        if state == "SUCCESS":
            return self.parser.parse(job_id=job_id)

        if state == "ERROR":
            return {
                "status": "ERROR",
                "job_id": job_id,
                "message": "Sandbox analysis failed"
            }

        return {
            "status": "UNKNOWN",
            "job_id": job_id,
            "message": f"Unexpected sandbox state: {state}"
        }


class QuickScanOrchestrator:
    """
    Quick Scan analiz akışını uçtan uca yöneten orchestration katmanı.
    """

    def __init__(self, client: APIClient):
        self.client = client
        self.submission = QuickScanService(client)
        self.poller = QuickScanPoller(client)
        self.parser = QuickScanParser()

    def run_file(
        self,
        file_path: str,
        scan_type: str = "all",
    ) -> dict:
        """
        Dosya için quick scan akışını çalıştırır.
        """

        # 1. Submit
        submit_resp = self.submission.scan_file(
            file_path=file_path,
            scan_type=scan_type
        )

        scan_id = submit_resp.get("id")
        if not scan_id:
            raise RuntimeError("Quick scan submission did not return id")

        # 2. Poll (finished == true)
        final_resp = self.poller.wait(scan_id)

        # 3. Parse
        return self.parser.parse(final_resp)


    def run_url(
        self,
        url: str,
        scan_type: str = "all",
    ) -> dict:
        """
        URL için quick scan akışını çalıştırır.
        """

        # 1. Submit
        submit_resp = self.submission.scan_url(
            url=url,
            scan_type=scan_type
        )

        scan_id = submit_resp.get("id")
        if not scan_id:
            raise RuntimeError("Quick scan submission did not return id")

        # 2. Poll
        final_resp = self.poller.wait(scan_id)

        # 3. Parse
        return self.parser.parse(final_resp)


class SearchOrchestrator:
    """
    Search akışını yöneten orchestration katmanı.
    CLI'den gelen target_type kararına göre SearchService'i çağırır.
    """

    def __init__(self, client: APIClient):
        self.search = SearchService(client)

    def run_search(self, target: str, target_type: TargetType) -> dict:
        # filename: classifier YOK
        if target_type == TargetType.FILENAME:
            return self.search.search_by_filename(target)

        # explicit (--hash, --url, --domain, --host)
        return self.search.search(target, target_type)
