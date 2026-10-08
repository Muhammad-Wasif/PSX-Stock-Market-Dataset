# Pakistan Stock Exchange (PSX) Historical Stock Market Dataset

[![Author](https://img.shields.io/badge/Author-Muhammad%20Wasif-blue.svg)](https://github.com/Muhammad-Wasif)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Dataset](https://img.shields.io/badge/Dataset-10%20Years%20Daily%20OHLCV-orange.svg)](#)

A comprehensive historical daily dataset for the **Pakistan Stock Exchange (PSX)** covering **105 constituent companies** of the benchmark **KSE-100 Index** spanning **2016 through 2026** (~10 years of trading sessions, 239,461+ total rows).

Created and maintained by **[Muhammad Wasif](https://github.com/Muhammad-Wasif)**.

---

## ⚡ Quickstart: Direct Access in Python (Kaggle Style)

Just like Kaggle, you can directly load any company or the entire dataset into **pandas** in **1 single line of Python** without downloading or cloning anything:

### 1. Load an Individual Company
```python
import pandas as pd

# Directly read any company from GitHub Raw URL
url = "https://raw.githubusercontent.com/Muhammad-Wasif/PSX-Stock-Market-Dataset/main/stocks/Oil%20%26%20Gas%20Development%20Company%20Limited.csv"
df = pd.read_csv(url)

print(df.tail())
```

### 2. Load the Master Combined Dataset (All 105 Stocks, 239,461 Rows)
```python
import pandas as pd

# Load complete unified dataset across all 105 companies
url = "https://raw.githubusercontent.com/Muhammad-Wasif/PSX-Stock-Market-Dataset/main/combined/PSX_KSE100_Full_Historical_Daily.csv"
master_df = pd.read_csv(url)

print(f"Total Rows: {len(master_df):,}")
print(master_df.head())
```

### 3. Load Using the Built-In Python Helper (`psx_dataset.py`)
```python
from psx_dataset import load_stock, load_combined, list_companies

# Get list of all available companies
companies = list_companies()

# Load any company by name
sys_df = load_stock("Systems Limited")
engro_df = load_stock("Engro Corporation Limited")
```

---

## 💻 1-Line Terminal Download & Extract (`stock.zip`)

If you want to download and export the entire dataset directly into your current working terminal folder:

### 🐧 Linux / macOS (Bash)
```bash
curl -L -o stock.zip https://github.com/Muhammad-Wasif/PSX-Stock-Market-Dataset/raw/main/stock.zip && unzip -q stock.zip && rm stock.zip
```
*Or using `wget`:*
```bash
wget -O stock.zip https://github.com/Muhammad-Wasif/PSX-Stock-Market-Dataset/raw/main/stock.zip && unzip -q stock.zip && rm stock.zip
```

### 🪟 Windows (PowerShell)
```powershell
Invoke-WebRequest -Uri "https://github.com/Muhammad-Wasif/PSX-Stock-Market-Dataset/raw/main/stock.zip" -OutFile "stock.zip"; Expand-Archive -Path "stock.zip" -DestinationPath "."; Remove-Item "stock.zip"
```

### 🐍 Python (Cross-Platform 1-Liner)
```python
python -c "import urllib.request, zipfile, os; urllib.request.urlretrieve('https://github.com/Muhammad-Wasif/PSX-Stock-Market-Dataset/raw/main/stock.zip', 'stock.zip'); zipfile.ZipFile('stock.zip').extractall('.'); os.remove('stock.zip'); print('PSX Stock datasets extracted!')"
```

---

## 📁 Repository Structure

```
PSX-Stock-Market-Dataset/
├── stock.zip                                     # Ready-to-download complete zip archive (~6.8 MB)
├── psx_dataset.py                                # Python SDK to load files directly or download all
├── download_psx_dataset.py                       # Self-updating data fetcher script
├── combined/
│   └── PSX_KSE100_Full_Historical_Daily.csv      # Single unified dataset of all 105 companies (239,461 rows)
├── stocks/                                       # 105 individual CSV files (named by full corporate name)
│   ├── Abbott Laboratories (Pakistan) Limited.csv
│   ├── Allied Bank Limited.csv
│   ├── Engro Corporation Limited.csv
│   ├── Engro Fertilizers Limited.csv
│   ├── Habib Bank Limited.csv
│   ├── Lucky Cement Limited.csv
│   ├── Meezan Bank Limited.csv
│   ├── Oil & Gas Development Company Limited.csv
│   ├── Pakistan Petroleum Limited.csv
│   ├── Pakistan State Oil Company Limited.csv
│   ├── Systems Limited.csv
│   └── ... (all 105 companies)
├── indices/                                      # Index constituent holdings & weights
│   ├── KSE100_Constituents.csv                   # 100 benchmark companies
│   ├── KSE30_Constituents.csv                    # Top 30 liquid large-caps
│   ├── KMI30_Constituents.csv                    # Islamic Shariah-compliant 30 companies
│   └── ALLSHR_Constituents.csv                   # Complete 559 active exchange companies
├── metadata/                                     # Market structure & classifications
│   ├── PSX_Company_Name_To_Symbol_Mapping.csv    # Cross-reference of symbol, full name, and filename
│   ├── PSX_All_Listed_Companies.csv              # 1,038 listed equities, GEM, ETFs & debt securities
│   └── PSX_Sectors_Summary.csv                   # Sector listings & categorizations
└── README.md                                     # Documentation
```

---

## 📊 Data Schema

Each company CSV file contains clean, chronologically ordered daily trading records:

| Column | Type | Description |
| :--- | :--- | :--- |
| `company_name` | String | Full corporate name (e.g. `Oil & Gas Development Company Limited`) |
| `symbol` | String | Exchange ticker symbol (e.g. `OGDC`, `ENGRO`, `SYS`) |
| `date` | Date (`YYYY-MM-DD`) | Trading session date |
| `open` | Float | Session opening price in PKR |
| `high` | Float | Highest recorded price during the session in PKR |
| `low` | Float | Lowest recorded price during the session in PKR |
| `close` | Float | Final closing price in PKR |
| `volume` | Integer | Total number of shares traded during the session |
| `is_anomaly`| Boolean | Automated flag identifying data validation alerts |

---

## 👨‍💻 Author & Maintainer

* **Creator:** [Muhammad Wasif](https://github.com/Muhammad-Wasif)
* **GitHub Profile:** https://github.com/Muhammad-Wasif
* **Email:** wasifalibhatti12517@gmail.com
* **Project Repository:** https://github.com/Muhammad-Wasif/PSX-Stock-Market-Dataset

---

## 📜 License
This project and dataset are distributed under the MIT License.
