from pathlib import Path

from load_data import load_stocks
from metrics import prepare_returns, calculate_summary
from visualization import plot_returns, plot_risk_return, plot_price_history

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUTS_DIR = PROJECT_ROOT / "outputs"

START_DATE = "2015-01-01"


def main():
    OUTPUTS_DIR.mkdir(exist_ok=True)

    tickers = ["AAPL", "MSFT", "AMZN", "AMD", "AVGO", "ADBE"]

    stocks = load_stocks(tickers)
    stocks = stocks[stocks["Date"] >= START_DATE]
    stocks = prepare_returns(stocks)

    start_year = stocks["Date"].dt.year.min()
    end_year = stocks["Date"].dt.year.max()

    summary = calculate_summary(stocks)

    print("\nSummary:\n")
    print(summary.round(4))

    best_ticker = summary.index[0]
    best_sharpe = summary["Sharpe Ratio"].iloc[0]
    print(f"\nBest risk-adjusted performer: {best_ticker} (Sharpe: {best_sharpe:.2f})")

    summary.to_csv(OUTPUTS_DIR / "summary.csv")

    plot_returns(summary, start_year, end_year)
    plot_risk_return(summary, start_year, end_year)
    plot_price_history(stocks, start_year, end_year)

    print(f"\nResults saved to: {OUTPUTS_DIR}")


if __name__ == "__main__":
    main()
