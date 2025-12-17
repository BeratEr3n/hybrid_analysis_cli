# hybrit_analysis_cli

`hybrit_analysis_cli`, **Hybrid Analysis** API’sini kullanarak:

- sandbox submission (dosya / URL)
- quick scan (dosya / URL)
- hash / domain / ip / url / filename search

işlemlerini komut satırından veya programatik olarak (MCP / LLM) yapmanı sağlayan bir CLI aracıdır.

---

## Features

- Dosya ve URL için Sandbox Analizi
- Dosya ve URL için Quick Scan
- Hash / URL / Domain / IP / Filename arama
- Explicit target seçimi (otomatik tespit yok)
- API key zorunlu, fail-fast davranış

---

## Installation

### Repo’yu klonla
```bash
git clone https://github.com/BeratEr3n/hybrit_analysis_cli.git
cd hybrit_analysis_cli
```

### Virtual environment (önerilir)
```bash
python -m venv venv
venv\Scripts\activate
```

### Bağımlılıkları yükle
```bash
pip install -r requirements.txt
```

---

## Configuration

Bu projede:

- `.env` kullanılmaz
- environment variable kullanılmaz
- API key parametre olarak zorunludur

API key:
https://hybrid-analysis.com

---

## Usage

```bash
python src/main.py --api-key YOUR_API_KEY <command> [options]
```

API key verilmezse program çalışmaz.

---

## Commands

### Sandbox Submit

Dosya:
```bash
python src/main.py --api-key YOUR_API_KEY submit --file sample.exe
```

URL:
```bash
python src/main.py --api-key YOUR_API_KEY submit --url https://example.com
```

Özel environment:
```bash
python src/main.py --api-key YOUR_API_KEY submit --file sample.exe --env-id 140
```

---

### Quick Scan

Dosya:
```bash
python src/main.py --api-key YOUR_API_KEY scan --file sample.exe
```

URL:
```bash
python src/main.py --api-key YOUR_API_KEY scan --url https://example.com
```

Özel scan type:
```bash
python src/main.py --api-key YOUR_API_KEY scan --file sample.exe --scan-type all
```

---

### Search

Filename:
```bash
python src/main.py --api-key YOUR_API_KEY search --filename test.exe
```

Hash:
```bash
python src/main.py --api-key YOUR_API_KEY search --hash <sha256>
```

URL / Domain / Host:
```bash
python src/main.py --api-key YOUR_API_KEY search --url https://example.com
python src/main.py --api-key YOUR_API_KEY search --domain example.com
python src/main.py --api-key YOUR_API_KEY search --host 8.8.8.8
```

---

## Notes

- Sandbox ve quick scan işlemleri polling ile takip edilir
- Timeout ve interval ayarları `config/settings.py` içindedir
- Tool MCP / LLM entegrasyonu için uygundur, insan CLI deneyimi öncelik değildir

---

## License

MIT
