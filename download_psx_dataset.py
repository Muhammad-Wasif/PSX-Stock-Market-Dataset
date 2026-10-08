"""
Pakistan Stock Exchange (PSX) Historical Dataset Downloader & Updater
Created and Maintained by: Muhammad Wasif
GitHub: https://github.com/Muhammad-Wasif
Repository: https://github.com/Muhammad-Wasif/PSX-Stock-Market-Dataset
"""

import os
import sys
import time
import re
import psxdata
import pandas as pd

AUTHOR = "Muhammad Wasif"
GITHUB_PROFILE = "https://github.com/Muhammad-Wasif"

# Fix Windows console UTF-8 encoding
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

base_dir = os.path.dirname(os.path.abspath(__file__))
stocks_dir = os.path.join(base_dir, "stocks")
indices_dir = os.path.join(base_dir, "indices")
metadata_dir = os.path.join(base_dir, "metadata")
combined_dir = os.path.join(base_dir, "combined")

for d in [stocks_dir, indices_dir, metadata_dir, combined_dir]:
    os.makedirs(d, exist_ok=True)

print(f"=== PSX Historical Dataset Downloader by {AUTHOR} ===")

def clean_company_name(name):
    cleaned = name.replace('-', ' ').replace('_', ' ')
    cleaned = re.sub(r'[\\/*?:"<>|]', '', cleaned)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned

print("=== 1. Reading Index Constituents ===")
kse100_csv = os.path.join(indices_dir, "KSE100_Constituents.csv")
if os.path.exists(kse100_csv):
    kse100_df = pd.read_csv(kse100_csv)
    raw_symbols = kse100_df['symbol'].dropna().unique().tolist()
else:
    kse100_df = psxdata.indices('KSE100')
    kse100_df.to_csv(kse100_csv, index=False)
    raw_symbols = kse100_df['symbol'].dropna().unique().tolist()

clean_symbols = []
for s in raw_symbols:
    cleaned = re.sub(r'(XD|XB|XR)$', '', s.strip())
    clean_symbols.append((s, cleaned))

bluechips = [
    "OGDC", "PPL", "PSO", "LUCK", "ENGRO", "FFC", "EFERT", "MCB", "HBL", "UBL",
    "MEBL", "SYS", "TRG", "HUBC", "KAPCO", "DGKC", "CHCC", "SEARL", "MARI", "ATRL",
    "INDU", "HCAR", "PAEL", "UNITY", "NATF", "FCCL", "MLCF", "KOHC", "NML", "ILP",
    "POL", "LOTCHEM", "EPCL", "PRL", "SNGP", "SSGC", "BAFL", "BAHL", "BIPL", "FABL"
]
for bc in bluechips:
    if not any(bc == c for _, c in clean_symbols):
        clean_symbols.append((bc, bc))

seen = set()
unique_symbols = []
for raw, clean in clean_symbols:
    if clean not in seen:
        seen.add(clean)
        unique_symbols.append((raw, clean))

print(f"Total Unique PSX Stocks to Process: {len(unique_symbols)}")

all_dfs = []
success_count = 0

for i, (raw_sym, clean_sym) in enumerate(unique_symbols, 1):
    raw_name = clean_sym
    if kse100_df is not None and 'symbol' in kse100_df.columns:
        match = kse100_df[kse100_df['symbol'].str.startswith(clean_sym)]
        if not match.empty:
            raw_name = match.iloc[0]['name']
            
    full_name = clean_company_name(raw_name)
    csv_path = os.path.join(stocks_dir, f"{full_name}.csv")

    if os.path.exists(csv_path) and os.path.getsize(csv_path) > 500:
        try:
            df = pd.read_csv(csv_path)
            if not df.empty and 'date' in df.columns:
                df['date'] = pd.to_datetime(df['date'])
                all_dfs.append(df)
                success_count += 1
                print(f"[{i:03d}/{len(unique_symbols):03d}] Cached: '{full_name}' ({len(df)} rows)")
                continue
        except Exception:
            pass

    print(f"[{i:03d}/{len(unique_symbols):03d}] Fetching '{full_name}'...", end="", flush=True)
    df = None
    for try_sym in [clean_sym, raw_sym]:
        try:
            df = psxdata.stocks(try_sym)
            if df is not None and not df.empty:
                break
        except Exception:
            pass
    
    if df is not None and not df.empty:
        try:
            if 'date' in df.columns:
                df['date'] = pd.to_datetime(df['date'])
                df = df.sort_values(by='date').reset_index(drop=True)
            
            df.insert(0, 'company_name', full_name)
            df.insert(1, 'symbol', clean_sym)
            df.to_csv(csv_path, index=False)
            all_dfs.append(df)
            success_count += 1
            print(f" SUCCESS ({len(df)} rows)")
        except Exception as e:
            print(f" Error: {e}")
    else:
        print(" Empty")
    time.sleep(0.05)

if all_dfs:
    combined_master = pd.concat(all_dfs, ignore_index=True)
    combined_master_path = os.path.join(combined_dir, "PSX_KSE100_Full_Historical_Daily.csv")
    combined_master.to_csv(combined_master_path, index=False)
    print(f"\nSaved Master Combined Dataset: {combined_master_path} ({len(combined_master):,} rows)")

print(f"\nAll operations completed successfully by {AUTHOR}!")
