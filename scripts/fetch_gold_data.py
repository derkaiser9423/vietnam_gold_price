import os
import sqlite3
import requests
from datetime import datetime

API_BASE = "https://vn-gold-price-api-jvbw.onrender.com/api"  # May God help this host still alive
SOURCES = ["sjc", "doji", "pnj"]
DB_PATH = "data/metals_data.db"

def init_db():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS gold_prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT,
            gold_type TEXT,
            buy REAL,
            sell REAL,
            updated_at TEXT
        )
    """)
    conn.commit()
    conn.close()

def fetch_data(source):
    url = f"{API_BASE}/{source}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"⚠️ Failed to fetch data from {source}: {response.status_code}")
        return []
    data = response.json()
    updated_at = data.get("updatedAt", datetime.utcnow().isoformat())
    entries = []
    for item in data.get("data", []):
        entries.append((source.upper(), item["type"], item["buy"], item["sell"], updated_at))
    return entries

def store_data(entries):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.executemany("""
        INSERT INTO gold_prices (source, gold_type, buy, sell, updated_at)
        VALUES (?, ?, ?, ?, ?)
    """, entries)
    conn.commit()
    conn.close()

def main():
    print("🌕 Starting Vietnamese Gold Price update...")
    init_db()
    all_entries = []
    for src in SOURCES:
        all_entries += fetch_data(src)
    if all_entries:
        store_data(all_entries)
        print(f"✅ Successfully saved {len(all_entries)} records.")
    else:
        print("⚠️ No data fetched — check API endpoints or network.")

if __name__ == "__main__":
    main()
