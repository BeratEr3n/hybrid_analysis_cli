# src/core/poller.py

import time
from core.api import APIClient


class ReportPoller:
    """
    Sandbox analizinin tamamlanmasını bekleyen poller.
    Sadece report state kontrol eder.
    """

    TERMINAL_STATES = {"SUCCESS", "ERROR"}

    def __init__(
        self,
        client: APIClient,
        interval: int = 10,
        timeout: int = 600,
    ):
        """
        interval: kaç saniyede bir kontrol edilecek
        timeout: maksimum bekleme süresi (saniye)
        """
        self.client = client
        self.interval = interval
        self.timeout = timeout

    def wait(self, job_id: str) -> dict:
        """
        Analiz bitene kadar bekler ve final summary döner.
        """

        start_time = time.time()

        while True:
            response = self.client.get(
                path=f"/report/{job_id}/summary"
            )

            state = response.get("state")

            if state in self.TERMINAL_STATES:
                return response

            if time.time() - start_time > self.timeout:
                raise TimeoutError(
                    f"Analysis did not finish within {self.timeout} seconds"
                )

            time.sleep(self.interval)
