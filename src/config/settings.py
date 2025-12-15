#src/config/settings.py

import os
from pathlib import Path
from dotenv import load_dotenv

# Env
load_dotenv()
API_KEY = os.getenv("HYBRIT_ANALYSIS_API_KEY")

# Timeouts
TIMEOUT = int(60)

SANDBOX_INTERVAL = int(10)
SANDBOX_TIMEOUT = TIMEOUT*10

QUICKSCAN_INTERVAL = int(5)
QUICKSCAN_TIMEOUT = TIMEOUT*5


# Output dir
ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "outputs"

# Environment ID
environment_id = 140