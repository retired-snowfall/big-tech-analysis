import pandas as pd

# Assumed annual risk-free rate used to calculate excess returns.
# 2% is a rough long-term approximation of short-term US Treasury yields;
# adjust if you want to reflect a specific period more precisely.
RISK_FREE_RATE_ANNUAL = 0.02

# Number of trading days in a year, used to annualize daily statistics.
TRADING_DAYS_PER_YEAR = 252


def prepare_returns(stocks):
    """Sort by ticker/date and compute daily percentage returns per ticker."""
    stocks = stocks.sort_values(["Ticker", "Date"])
    stocks["Return"] = stocks.groupby("Ticker")["Close"].pct_change()
    return stocks


def calculate_summary(stocks, risk_free_annual=RISK_FREE_RATE_ANNUAL):
    """Calculate total return, volatility, and annualized Sharpe Ratio per ticker.

    Sharpe Ratio here is computed as:
        (mean daily excess return / std of daily returns) * sqrt(252)

    where "excess return" is the daily return minus the daily risk-free rate.
    This annualizes the metric so it's comparable to commonly reported
    (yearly) Sharpe Ratios, rather than reporting a raw daily figure.
    """
    first_price = stocks.groupby("Ticker")["Close"].first()
    last_price = stocks.groupby("Ticker")["Close"].last()

    total_return = (last_price - first_price) / first_price * 100

    grouped = stocks.groupby("Ticker")["Return"]
    daily_mean = grouped.mean()
    daily_std = grouped.std()

    volatility = daily_std * 100

    risk_free_daily = risk_free_annual / TRADING_DAYS_PER_YEAR
    excess_daily_return = daily_mean - risk_free_daily
    sharpe_ratio = (excess_daily_return / daily_std) * (TRADING_DAYS_PER_YEAR ** 0.5)

    summary = pd.DataFrame({
        "Total Return (%)": total_return,
        "Volatility (%)": volatility,
        "Sharpe Ratio": sharpe_ratio
    })
    return summary.sort_values("Sharpe Ratio", ascending=False)
