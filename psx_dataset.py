"""
Pakistan Stock Exchange (PSX) Historical Dataset Loader
Created and Maintained by: Muhammad Wasif
GitHub: https://github.com/Muhammad-Wasif
Repository: https://github.com/Muhammad-Wasif/PSX-Stock-Market-Dataset
"""

import urllib.parse
import urllib.request
import zipfile
import os
import io
import pandas as pd

AUTHOR = "Muhammad Wasif"
GITHUB_USER = "Muhammad-Wasif"
REPO_NAME = "PSX-Stock-Market-Dataset"
BRANCH = "main"

RAW_BASE_URL = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/{BRANCH}"
ZIP_DOWNLOAD_URL = f"https://github.com/{GITHUB_USER}/{REPO_NAME}/raw/{BRANCH}/stock.zip"


def load_stock(company_name: str) -> pd.DataFrame:
    """
    Directly load historical daily OHLCV dataset for a company from GitHub into pandas.
    Similar to Kaggle API datasets.
    
    Example:
        df = load_stock("Oil & Gas Development Company Limited")
        df = load_stock("Systems Limited")
    """
    # Clean company name: remove .csv if passed
    if company_name.endswith('.csv'):
        company_name = company_name[:-4]
    
    encoded_name = urllib.parse.quote(company_name)
    url = f"{RAW_BASE_URL}/stocks/{encoded_name}.csv"
    
    print(f"Loading '{company_name}' from: {url}")
    df = pd.read_csv(url)
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
    return df


def load_combined() -> pd.DataFrame:
    """
    Directly loads the master KSE-100 dataset (all 105 companies, 239k+ rows) into pandas.
    """
    url = f"{RAW_BASE_URL}/combined/PSX_KSE100_Full_Historical_Daily.csv"
    print(f"Loading Master Combined Dataset from: {url}")
    df = pd.read_csv(url)
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
    return df


def list_companies() -> pd.DataFrame:
    """
    Returns the complete list of 105 available PSX companies and ticker symbols.
    """
    url = f"{RAW_BASE_URL}/metadata/PSX_Company_Name_To_Symbol_Mapping.csv"
    return pd.read_csv(url)


def download_all(dest_folder: str = ".") -> None:
    """
    Downloads stock.zip from GitHub and extracts all datasets into dest_folder.
    """
    os.makedirs(dest_folder, exist_ok=True)
    zip_dest = os.path.join(dest_folder, "stock.zip")
    
    print(f"Downloading stock.zip from {ZIP_DOWNLOAD_URL}...")
    urllib.request.urlretrieve(ZIP_DOWNLOAD_URL, zip_dest)
    
    print(f"Extracting stock.zip into '{dest_folder}'...")
    with zipfile.ZipFile(zip_dest, 'r') as zip_ref:
        zip_ref.extractall(dest_folder)
    
    if os.path.exists(zip_dest):
        os.remove(zip_dest)
    print("All PSX datasets downloaded and extracted successfully!")


if __name__ == "__main__":
    print(f"Pakistan Stock Exchange Dataset SDK by {AUTHOR}")
    companies = list_companies()
    print(f"Loaded {len(companies)} registered companies.")
    print("Top 5 Companies:")
    print(companies.head())
