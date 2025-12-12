# src/core/submission.py

from pathlib import Path
from core.api import APIClient


class SubmissionService:
    """Sandbox submission (file / url) işlemlerini yöneten servis"""

    def __init__(self, client: APIClient):
        self.client = client

    def submit_file(
        self,
        file_path: str,
        environment_id: int,
        allow_community_access: bool = True,
    ) -> dict:
        path = "/submit/file"

        file_path = Path(file_path)
        if not file_path.exists() or not file_path.is_file():
            raise ValueError(f"File not found: {file_path}")

        files = {
            "file": file_path.open("rb")
        }

        data = {
            "environment_id": environment_id,
            "allow_community_access": int(allow_community_access),
        }

        try:
            return self.client.post(
                path=path,
                data=data,
                files=files,
            )
        finally:
            files["file"].close()


    def submit_url(
        self,
        url: str,
        environment_id: int
    ) -> dict:
        path = "/submit/url"

        data = {
            "url": url,
            "environment_id": environment_id
        }

        return self.client.post(
            path=path,
            data=data,
        )
