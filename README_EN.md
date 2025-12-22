# hybrid_analysis_cli

`hybrid_analysis_cli` is a CLI tool that uses the **Hybrid Analysis** API to perform:

- sandbox submission (file / URL)
- quick scan (file / URL)
- hash / domain / ip / url / filename search

from the command line or programmatically (MCP / LLM).

---

## Features

- File & URL Sandbox Analysis
- File & URL Quick Scan
- Hash / URL / Domain / IP / Filename search
- Explicit target selection (no auto-detection)
- API key required, fail-fast behavior

---

## Installation

### Clone the repository
```bash
git clone https://github.com/BeratEr3n/hybrid_analysis_cli.git
cd hybrid_analysis_cli
```

### Virtual environment (recommended)
```bash
python -m venv venv
venv\Scripts\activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

---

## Configuration

In this project:

- `.env` is not used
- Environment variables are not used
- API key is required as a parameter

API key:
https://hybrid-analysis.com

---

## Usage

```bash
python src/main.py --api-key YOUR_API_KEY <command> [options]
```

The program will not run without an API key.

---

## Commands

### Sandbox Submit

File:
```bash
python src/main.py --api-key YOUR_API_KEY --submit --file sample.exe
```

URL:
```bash
python src/main.py --api-key YOUR_API_KEY --submit --url https://example.com
```

Custom environment:
```bash
python src/main.py --api-key YOUR_API_KEY --submit --file sample.exe --env-id 140
```

---

### Quick Scan

File:
```bash
python src/main.py --api-key YOUR_API_KEY --scan --file sample.exe
```

URL:
```bash
python src/main.py --api-key YOUR_API_KEY --scan --url https://example.com
```

Custom scan type:
```bash
python src/main.py --api-key YOUR_API_KEY --scan --file sample.exe --scan-type all
```

---

### Search

Filename:
```bash
python src/main.py --api-key YOUR_API_KEY --search --filename test.exe
```

Hash:
```bash
python src/main.py --api-key YOUR_API_KEY --search --hash <sha256>
```

URL / Domain / Host:
```bash
python src/main.py --api-key YOUR_API_KEY --search --url https://example.com
python src/main.py --api-key YOUR_API_KEY --search --domain example.com
python src/main.py --api-key YOUR_API_KEY --search --host 8.8.8.8
```

---

## Notes

- Sandbox and quick scan operations are tracked via polling
- Timeout and interval settings are configured in `config/settings.py`
- The tool is designed for MCP / LLM integration; human CLI UX is not the priority

---

## License

MIT
