# hybrit_analysis_cli

`hybrit_analysis_cli`, **Hybrid Analysis** API’sini kullanarak
- sandbox submission
- quick scan
- hash / domain / ip / url / filename search

işlemlerini **komut satırından** yapmanı sağlayan bir CLI aracıdır.

---

## 🚀 Features

- File & URL **Sandbox Analysis**
- File & URL **Quick Scan**
- Hash / URL / Domain / IP / Filename **Search**
- Otomatik target type tespiti (`--target`)

---

## 📦 Installation

### 1. Repo’yu klonla
```bash
git clone https://github.com/BeratEr3n/hybrit_analysis_cli.git
cd hybrit_analysis_cli
```

### 2. Virtual environment (önerilir)
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Bağımlılıkları yükle
```bash
pip install -r requirements.txt
```

---

## 🔑 Configuration

### `.env` dosyası oluştur
```bash
cp .env.example .env
```

### `.env` içeriği
```env
HYBRIT_ANALYSIS_API_KEY=YOUR_API_KEY_HERE
```

> API key: https://hybrid-analysis.com

---

## ▶️ Usage

```bash
python src/main.py <command> [options]
```

---

## 🧪 Commands

### 🔹 Sandbox Submit

#### File
```bash
python src/main.py submit --file sample.exe
```

#### URL
```bash
python src/main.py submit --url https://example.com
```

#### Custom environment
```bash
python src/main.py submit --file sample.exe --env-id 140
```

---

### 🔹 Quick Scan

#### File
```bash
python src/main.py scan --file sample.exe
```

#### URL
```bash
python src/main.py scan --url https://example.com
```

#### Custom scan type
```bash
python src/main.py scan --file sample.exe --scan-type all
```

---

### 🔹 Search

#### Filename
```bash
python src/main.py search --filename test.exe
```

#### Hash
```bash
python src/main.py search --hash <sha256>
```

#### URL / Domain / Host
```bash
python src/main.py search --url https://example.com
python src/main.py search --domain example.com
python src/main.py search --host 8.8.8.8
```

#### Auto-detect
```bash
python src/main.py search --target example.com
```

---


## 🛠 Notes

- Sandbox & quick scan işlemleri **polling** ile takip edilir
- Timeout ve interval ayarları `config/settings.py` içindedir
- Parser katmanları ileride zenginleştirilmek üzere sade tutulmuştur

---

## 📄 License

MIT
