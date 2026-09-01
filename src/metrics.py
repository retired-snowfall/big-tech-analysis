import pandas as pd

RISK_FREE_RATE_ANNUAL = 0.02


def prepare_returns(stocks):
    stocks = stocks.sort_values(
        ["Ticker", "Date"]
    )

    stocks["Return"] = (
        stocks.groupby("Ticker")["Close"]
        .pct_change()
    )

    return stocks




def calculate_summary(stocks, risk_free_annual=RISK_FREE_RATE_ANNUAL):
    first_price = stocks.groupby("Ticker")["Close"].first()
    last_price = stocks.groupby("Ticker")["Close"].last()

    total_return = (last_price - first_price) / first_price * 100

    grouped = stocks.groupby("Ticker")["Return"]
    daily_std = grouped.std()
    volatility = daily_std * 100

    risk_free_daily = risk_free_annual / 252
    excess_daily_return = grouped.mean() - risk_free_daily

    sharpe_ratio = (excess_daily_return / daily_std) * (252 ** 0.5)

    summary = pd.DataFrame({
        "Total Return (%)": total_return,
        "Volatility (%)": volatility,
        "Sharpe Ratio": sharpe_ratio
    })
    return summary.sort_values("Sharpe Ratio", ascending=False)
