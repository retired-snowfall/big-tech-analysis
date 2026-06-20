from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"


def load_stocks(tickers):
    dfs = []

    for ticker in tickers:
        file_path = DATA_DIR / f"{ticker}.csv"

        df = pd.read_csv(file_path)
        df["Ticker"] = ticker

        dfs.append(df)

    stocks = pd.concat(dfs, ignore_index=True)

    stocks["Date"] = pd.to_datetime(
        stocks["Date"],
        utc=True
    )

    return stocks