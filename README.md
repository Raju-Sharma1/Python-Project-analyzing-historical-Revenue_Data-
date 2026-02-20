# 📈 Tesla & GameStop Stock and Revenue Analysis

## 📌 Project Overview
This project analyzes historical stock data and revenue data for **Tesla (TSLA)** and **GameStop (GME)** using Python.  

The objective is to extract, clean, and store financial data using APIs and web scraping techniques, then prepare the data for further analysis and visualization.

---

## 🚀 Tasks Performed

### 🔹 Task 1: Extract Tesla Stock Data
- Used `yfinance` API to retrieve historical stock data for **TSLA**
- Extracted maximum available historical data
- Reset index for structured analysis

### 🔹 Task 2: Extract Tesla Revenue Data (Web Scraping)
- Scraped revenue data from HTML source using:
  - `requests`
  - `BeautifulSoup`
- Cleaned revenue column (removed `$` and `,`)
- Removed null and empty values
- Saved cleaned data to: "tesla_revenue.csv"

### 🔹 Task 3: Extract GameStop Stock Data
- Used `yfinance` API to retrieve historical stock data for **GME**
- Extracted maximum available data
- Reset index for structured analysis

### 🔹 Task 4: Extract GameStop Revenue Data (Web Scraping)
- Scraped revenue data using `BeautifulSoup`
- Cleaned revenue column (removed `$` and `,`)
- Removed null and empty values
- Saved cleaned data to: "gme_revenue.csv"


---

## 🛠️ Technologies Used
- Python
- Pandas
- yfinance API
- Requests
- BeautifulSoup

---

## 📂 Output Files
- `tesla_revenue.csv`
- `gme_revenue.csv`

---

## 📊 Skills Demonstrated
- API Data Extraction
- Web Scraping
- Data Cleaning & Transformation
- Data Storage (CSV Export)
- Financial Data Analysis

---

## 🎯 Project Objective
To demonstrate practical implementation of:
- Financial data extraction
- Web scraping techniques
- Data wrangling using Pandas
- Preparing datasets for visualization and business insights
