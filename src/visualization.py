from pathlib import Path
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUTS_DIR = PROJECT_ROOT / "outputs"


def plot_returns(summary, start_year, end_year):
    plt.figure(figsize=(10, 6))
    summary["Total Return (%)"].sort_values().plot(kind="bar")
    plt.title(f"Big Tech Total Return ({start_year}-{end_year})")
    plt.xlabel("Ticker")
    plt.ylabel("Return (%)")
    plt.tight_layout()
    plt.savefig(OUTPUTS_DIR / "return_chart.png", dpi=300, bbox_inches="tight")
    plt.close()


def plot_risk_return(summary, start_year, end_year):
    plt.figure(figsize=(10, 6))
    plt.scatter(summary["Volatility (%)"], summary["Total Return (%)"])

    for ticker in summary.index:
        plt.annotate(
            ticker,
            (summary.loc[ticker, "Volatility (%)"], summary.loc[ticker, "Total Return (%)"])
        )

    plt.xlabel("Volatility (%)")
    plt.ylabel("Total Return (%)")
    plt.title(f"Risk vs Return ({start_year}-{end_year})")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(OUTPUTS_DIR / "risk_return_chart.png", dpi=300, bbox_inches="tight")
    plt.close()


def plot_price_history(stocks, start_year, end_year):
    """Plot normalized closing prices over time for all tickers.

    Prices are normalized to a base of 100 at the start of the period so
    companies with very different share prices can be compared on the
    same chart.
    """
    plt.figure(figsize=(12, 7))

    for ticker, group in stocks.groupby("Ticker"):
        group = group.sort_values("Date")
        normalized = group["Close"] / group["Close"].iloc[0] * 100
        plt.plot(group["Date"], normalized, label=ticker)

    plt.title(f"Normalized Price History ({start_year}-{end_year}, base = 100)")
    plt.xlabel("Date")
    plt.ylabel("Normalized Price")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(OUTPUTS_DIR / "price_history_chart.png", dpi=300, bbox_inches="tight")
    plt.close()
