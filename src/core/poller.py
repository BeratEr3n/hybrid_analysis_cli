# src/core/poller.py

import time
from core.api import APIClient
from config.settings import SANDBOX_INTERVAL, SANDBOX_TIMEOUT, QUICKSCAN_INTERVAL , QUICKSCAN_TIMEOUT

class SandboxPoller:
    """
    Sandbox analizinin tamamlanmasını bekleyen poller.
    SADECE report state endpoint'ini kullanır.
    """

    TERMINAL_STATES = {"SUCCESS", "ERROR"}

    def __init__(
        self,
        client: APIClient,
        interval: int = SANDBOX_INTERVAL,
        timeout: int = SANDBOX_TIMEOUT,
    ):
        """
        interval: kaç saniyede bir state kontrol edilecek
        timeout: maksimum bekleme süresi (saniye)
        """
        self.client = client
        self.interval = interval
        self.timeout = timeout

    def wait(self, job_id: str) -> str: 
        """
        Analiz tamamlanana kadar bekler.
        Terminal state (SUCCESS / ERROR) döner.
        """

        start_time = time.time()

        while True:
            response = self.client.get(
                path=f"/report/{job_id}/state"
            )

            state = response.get("state")

            if state in self.TERMINAL_STATES:
                return state

            # Debug için daha sonra kaldırılabiliriz.
            if state == "IN_PROGRESS":
                print("Üzerinde Çalışılıyor: ", int(time.time() - start_time),"sn")

            if time.time() - start_time > self.timeout:
                raise TimeoutError(
                    f"Analysis did not finish within {self.timeout} seconds"
                )

            time.sleep(self.interval)



class QuickScanPoller:
    """
    Quick Scan işleminin tamamlanmasını bekleyen poller.
    """

    def __init__(
        self,
        client: APIClient,
        interval: int = QUICKSCAN_INTERVAL,
        timeout: int = QUICKSCAN_TIMEOUT,
    ):
        self.client = client
        self.interval = interval
        self.timeout = timeout

    def wait(self, scan_id: str) -> dict:
        """
        finished == true olana kadar /quick-scan/{id} endpoint'ini poll eder.
        """

        start_time = time.time()

        while True:
            response = self.client.get(
                path=f"/quick-scan/{scan_id}"
            )

            finished = response.get("finished", False)
            
            if finished is False:
                print("Üzerinde Çalışılıyor: ", int(time.time() - start_time),"sn")
            
            if finished is True:
                return response

            if time.time() - start_time > self.timeout:
                raise TimeoutError(
                    f"Quick scan did not finish within {self.timeout} seconds"
                )

            time.sleep(self.interval)
