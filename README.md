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

Summary table for the 2015–2023 period, sorted by Sharpe Ratio:

| Ticker | Total Return (%) | Volatility (%) | Sharpe Ratio |
| ------ | ----------------: | ---------------: | -------------: |
| AMD    | 3518.35            | 3.79              | 0.9456          |
| MSFT   | 691.99             | 1.77              | 0.9168          |
| AVGO   | 927.98             | 2.22              | 0.8805          |
| AAPL   | 614.79             | 1.85              | 0.8485          |
| AMZN   | 747.01             | 2.10              | 0.8416          |
| ADBE   | 613.89             | 2.07              | 0.7907          |

Full results are exported automatically to:

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

- **AMD delivered by far the highest total return (3518%)** over the period, alongside the highest volatility (3.79%) of the group — consistent with its exposure to cyclical semiconductor demand and, more recently, AI/data-center growth.
- **Despite the elevated risk, AMD also had the highest Sharpe Ratio (0.95)**, meaning its outsized returns more than compensated for the extra volatility — the risk was, in hindsight, well rewarded.
- **MSFT stands out on the other end**: the lowest volatility in the group (1.77%) combined with solid, steady returns gives it the second-highest Sharpe Ratio (0.92) — a case of consistency competing effectively with raw growth.
- **AVGO posted the second-highest total return (928%)** with moderate volatility, landing in the middle of the risk-adjusted ranking.
- **AAPL, AMZN, and ADBE cluster closely together** on both return and volatility, with Sharpe Ratios in a narrow 0.79–0.85 band — none of them stands out sharply from the others on a risk-adjusted basis.
- Overall, the risk-vs-return scatter plot makes the trade-off visible at a glance: AMD sits far out on both axes, while the rest of the group occupies a much tighter, lower-risk region.

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
