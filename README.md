# 🇻🇳 Vietnamese Gold Price Tracker 🪙

[![Daily Gold Price Collection](https://github.com/derkaiser9423/vietnam_gold_price/actions/workflows/collect_data.yml/badge.svg)](https://github.com/derkaiser9423/vietnam_gold_price/actions/workflows/collect_data.yml)

> Automated daily updates of Vietnamese gold prices from **SJC**, **DOJI**, and **PNJ**, stored in a structured SQLite database.

---

## 🧭 Overview

This project automatically collects gold prices from major Vietnamese markets and keeps them in a local SQLite database, updated daily at **2 PM Vietnam time**.

It uses:
- **GitHub Actions** to automate daily data fetching  
- **Custom Vietnamese Gold Price API** as the source  
- **SQLite** for lightweight data storage  

---
📊 Database Schema
Column	Type	Description
id	INTEGER	Auto-increment primary key
source	TEXT	Gold vendor (SJC / DOJI / PNJ)
gold_type	TEXT	Type of gold
buy	REAL	Buying price
sell	REAL	Selling price
updated_at	TEXT	Timestamp of last update
🧰 Usage

After the workflow runs, download data/metals_data.db and query it locally:

SELECT source, gold_type, buy, sell, updated_at
FROM gold_prices
ORDER BY updated_at DESC
LIMIT 10;

