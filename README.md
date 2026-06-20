# Big Tech Stock Analysis (2015–2026)

## Overview

This project analyzes historical stock performance of major U.S. technology companies and compares them using key financial metrics:

- Total return
- Volatility (risk)
- Risk-adjusted efficiency (Return / Volatility)

The objective is to evaluate which companies provided the best balance between return and risk over the selected time period.

---

## Dataset

The dataset contains daily historical stock prices for the following companies:

- Apple (AAPL)
- Microsoft (MSFT)
- Amazon (AMZN)
- AMD (AMD)
- Broadcom (AVGO)
- Adobe (ADBE)

Source: Yahoo Finance (Kaggle dataset)

---

## Methodology

1. Load and merge multiple CSV files.
2. Convert date columns to datetime format (UTC).
3. Filter data starting from 2015.
4. Compute daily returns using percentage change.
5. Calculate the following metrics:
   - Total return
   - Volatility (standard deviation of returns)
   - Risk-adjusted efficiency (Return / Volatility)
6. Generate visualizations of results.

---

## Results

### Risk-Adjusted Ranking (Return / Volatility)

| Rank | Ticker | Score |
|------|--------|-------|
| 1 | AMD  | 928 |
| 2 | AVGO | 419 |
| 3 | MSFT | 392 |
| 4 | AMZN | 355 |
| 5 | AAPL | 332 |
| 6 | ADBE | 296 |

---

## Observations

- AMD achieved the highest total return but also exhibited the highest volatility.
- Microsoft showed the most balanced risk-return profile.
- Amazon and Apple demonstrated consistent performance with moderate efficiency.
- Adobe had the lowest risk-adjusted performance in this sample.

---

## Visualizations

### Total Return Comparison

![Total Return](outputs/return_chart.png)

### Risk vs Return

![Risk vs Return](outputs/risk_return_chart.png)

---

## Metrics Definition

- **Total Return (%)**: Overall percentage growth from 2015 to 2026.
- **Volatility (%)**: Standard deviation of daily returns.
- **Return / Volatility**: Custom efficiency metric measuring return per unit of risk.

---

big-tech-analysis/
├── data/
│   ├── AAPL.csv
│   ├── ADBE.csv
│   ├── AMD.csv
│   ├── AMZN.csv
│   ├── AVGO.csv
│   └── MSFT.csv
│
├── outputs/
│   ├── return_chart.png
│   ├── risk_return_chart.png
│   └── summary.csv
│
├── src/
│   ├── load_data.py
│   ├── metrics.py
│   ├── visualization.py
│   └── main.py
│
├── README.md
├── requirements.txt
└── .gitignore




---

## How to Run

```bash
git clone https://github.com/your-username/big-tech-analysis.git
cd big-tech-analysis

pip install -r requirements.txt
python src/main.py
