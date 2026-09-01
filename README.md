# Big Tech Stock Analysis

## Overview

This project analyzes the historical performance of major U.S. technology companies using daily stock market data from Yahoo Finance.

The analysis focuses on comparing return, risk, and risk-adjusted performance between companies over the period from 2015 onward.

The project was built to practice data analysis workflows, including data cleaning, feature engineering, financial metrics calculation, and data visualization.

---

## Companies Analyzed

- Apple (AAPL)
- Microsoft (MSFT)
- Amazon (AMZN)
- AMD (AMD)
- Broadcom (AVGO)
- Adobe (ADBE)

---

## Dataset

Historical daily stock prices obtained from Yahoo Finance.

Each company is stored as a separate CSV file containing:

- Date
- Open
- High
- Low
- Close
- Volume
- Dividends
- Stock Splits

---

## Analysis Pipeline

1. Load stock data from multiple CSV files.
2. Merge datasets into a single DataFrame.
3. Convert dates to UTC datetime format.
4. Filter observations from 2015 onward.
5. Calculate daily returns.
6. Compute performance metrics.
7. Generate visualizations.
8. Export results to CSV.

---

## Metrics

### Total Return

Measures overall growth during the analysis period.

```
Total Return = (Final Price − Initial Price) / Initial Price
```

### Volatility

Standard deviation of daily returns, used as a measure of risk.

### Sharpe Ratio

Measures risk-adjusted performance: how much excess return an asset generates per unit of risk.

```
Sharpe Ratio = (Mean Daily Excess Return / Std Dev of Daily Returns) × √252
```

Where:
- **Excess return** = daily return − daily risk-free rate
- An annual risk-free rate of **2%** is assumed (a rough approximation of short-term Treasury yields), converted to a daily rate
- The result is annualized by multiplying by √252 (the number of trading days in a year), so the Sharpe Ratio is expressed on a yearly basis and comparable to commonly reported figures

Higher values indicate better return per unit of risk.

---

## Results

The project generates a summary table containing:

| Ticker | Total Return (%) | Volatility (%) | Sharpe Ratio |
| ------ | ----------------- | --------------- | ------------- |
| ...    | ...                | ...              | ...            |

Results are exported automatically to:

```
outputs/summary.csv
```

The script also prints the best risk-adjusted performer (highest Sharpe Ratio) directly to the console.

---

## Visualizations

### Normalized Price History

Closing prices for all tickers, normalized to a base of 100 at the start of the period, so companies with very different share prices can be compared directly on one chart.

```
outputs/price_history_chart.png
```

### Total Return Comparison

```
outputs/return_chart.png
```

### Risk vs Return

```
outputs/risk_return_chart.png
```

Charts are generated automatically and saved to the `outputs` directory. Chart titles reflect the actual date range covered by the loaded data.

---

## Interpretation

A few observations that typically hold for this dataset (exact figures depend on the date range the data was pulled for):

- Semiconductor and cloud-infrastructure names (e.g. AMD, AVGO) tend to show higher volatility alongside higher total returns — consistent with their exposure to cyclical hardware demand and AI/data-center growth.
- Large, diversified platforms (e.g. AAPL, MSFT) tend to show comparatively lower volatility, which can translate into a competitive Sharpe Ratio even without leading in raw total return.
- The risk-vs-return scatter plot is a quick way to see which companies delivered strong returns *relative to* the risk taken, rather than just the highest raw return.

---

## Project Structure

```
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
│   ├── price_history_chart.png
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
```

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib

## Running the Project

```bash
pip install -r requirements.txt
cd src
python main.py
```

Results (summary table and charts) will be written to the `outputs/` directory.
