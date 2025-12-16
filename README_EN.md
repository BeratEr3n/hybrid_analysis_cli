# hybrit_analysis_cli

`hybrit_analysis_cli` is a command-line tool that uses the **Hybrid Analysis** API to perform:
- sandbox submissions
- quick scans
- hash / domain / IP / URL / filename searches

directly from the terminal.

---

## 🚀 Features

- File & URL **Sandbox Analysis**
- File & URL **Quick Scan**
- Hash / URL / Domain / IP / Filename **Search**
- Automatic target type detection (`--target`)

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/BeratEr3n/hybrit_analysis_cli.git
cd hybrit_analysis_cli
```

### 2. Virtual environment (recommended)
```bat
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🔑 Configuration

### Create `.env` file
```bat
copy .env.example .env
```

### `.env` content
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

- Sandbox and quick scan operations are handled via **polling**
- Timeout and interval settings are located in `config/settings.py`
- Parser layers are intentionally minimal and designed for future extension

---

## 📄 License

MIT
