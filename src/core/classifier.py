# src/core/classifier.py

from enum import Enum

class TargetType(str, Enum):
    HASH = "hash"
    HOST = "host"
    DOMAIN = "domain"
    URL = "url"
    FILENAME = "filename"
