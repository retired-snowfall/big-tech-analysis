from pathlib import Path

from load_data import load_stocks
from metrics import (
    prepare_returns,
    calculate_summary
)
from visualization import (
    plot_returns,
    plot_risk_return
)


PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUTS_DIR = PROJECT_ROOT / "outputs"


def main():
    OUTPUTS_DIR.mkdir(
        exist_ok=True
    )

    tickers = [
        "AAPL",
        "MSFT",
        "AMZN",
        "AMD",
        "AVGO",
        "ADBE"
    ]

    stocks = load_stocks(
        tickers
    )

    stocks = stocks[
        stocks["Date"] >= "2015-01-01"
    ]

    stocks = prepare_returns(
        stocks
    )

    summary = calculate_summary(
        stocks
    )

    print("\nSummary:\n")
    print(summary.round(4))

    summary.to_csv(
        OUTPUTS_DIR / "summary.csv"
    )

    plot_returns(summary)
    plot_risk_return(summary)

    print(
        f"\nResults saved to: {OUTPUTS_DIR}"
    )


if __name__ == "__main__":
    main()
