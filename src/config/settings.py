#src/config/settings.py
import os
from pathlib import Path
from dotenv import load_dotenv

# Env
load_dotenv()
API_KEY = os.getenv("HYBRIT_ANALYSIS_API_KEY")

# Timeout
TIMEOUT = int(60)

# Output dir
ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "outputs"

# Environment ID
environment_id = 140