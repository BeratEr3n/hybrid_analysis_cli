# src/core/classifier.py

import re
from enum import Enum


class TargetType(str, Enum):
    HASH = "hash"
    IP = "host"
    DOMAIN = "domain"
    URL = "url"
    UNKNOWN = "unknown"


class TargetClassifier:
    HASH_RE = re.compile(r"^[a-fA-F0-9]{32,128}$")
    IP_RE = re.compile(r"^\d{1,3}(\.\d{1,3}){3}$")

    def classify(self, value: str) -> TargetType:
        value = value.strip()

        if not value:
            return TargetType.UNKNOWN

        if value.startswith("http://") or value.startswith("https://"):
            return TargetType.URL

        if self.IP_RE.match(value):
            return TargetType.IP

        if self.HASH_RE.match(value):
            return TargetType.HASH

        # domain için basit ama yeterli kontrol
        if "." in value and " " not in value:
            return TargetType.DOMAIN

        return TargetType.UNKNOWN
