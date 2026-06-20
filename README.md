# Big Tech Stock Analysis

## Project Overview

This project analyzes the performance of major U.S. technology companies using historical stock market data from 2015 onward.

The analysis focuses on:

* Total return
* Daily returns
* Volatility (risk)
* Return-to-risk ratio

## Companies Analyzed

* Apple (AAPL)
* Microsoft (MSFT)
* Amazon (AMZN)
* AMD (AMD)
* Broadcom (AVGO)
* Adobe (ADBE)

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib

## Methodology

1. Load historical stock data from CSV files.
2. Convert dates to UTC.
3. Filter observations from 2015 onward.
4. Calculate daily returns using percentage change.
5. Calculate:

   * Total return
   * Volatility
   * Return/Risk ratio
6. Visualize results.

## Key Findings

* AMD delivered the highest total return during the analyzed period.
* Microsoft showed the lowest volatility among the selected companies.
* AMD achieved the strongest return-to-risk ratio.
* Adobe had the weakest return-to-risk performance among the selected stocks.

## Example Output

| Ticker | Total Return (%) | Volatility (%) | Return/Risk |
| ------ | ---------------: | -------------: | ----------: |
| AMD    |          3518.35 |           3.79 |      927.88 |
| AVGO   |           927.98 |           2.22 |      418.56 |
| MSFT   |           691.99 |           1.77 |      391.81 |
| AMZN   |           747.01 |           2.10 |      355.31 |
| AAPL   |           614.79 |           1.85 |      332.44 |
| ADBE   |           613.89 |           2.07 |      296.08 |

## Future Improvements

* Sharpe Ratio
* Maximum Drawdown
* Sector comparison
* Portfolio simulation
* Interactive dashboards
