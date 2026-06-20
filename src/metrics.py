import pandas as pd


def prepare_returns(stocks):
    stocks = stocks.sort_values(
        ["Ticker", "Date"]
    )

    stocks["Return"] = (
        stocks.groupby("Ticker")["Close"]
        .pct_change()
    )

    return stocks


def calculate_summary(stocks):
    first_price = (
        stocks.groupby("Ticker")["Close"]
        .first()
    )

    last_price = (
        stocks.groupby("Ticker")["Close"]
        .last()
    )

    total_return = (
        (last_price - first_price)
        / first_price
        * 100
    )

    volatility = (
        stocks.groupby("Ticker")["Return"]
        .std()
        * 100
    )

    summary = pd.DataFrame({
        "Total Return (%)": total_return,
        "Volatility (%)": volatility
    })

    summary["Return/Risk"] = (
        summary["Total Return (%)"]
        / summary["Volatility (%)"]
    )

    return summary.sort_values(
        "Return/Risk",
        ascending=False
    )