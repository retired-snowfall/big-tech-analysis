from pathlib import Path

import matplotlib.pyplot as plt


PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUTS_DIR = PROJECT_ROOT / "outputs"


def plot_returns(summary):
    plt.figure(figsize=(10, 6))

    summary["Total Return (%)"] \
        .sort_values() \
        .plot(kind="bar")

    plt.title(
        "Big Tech Total Return Since 2015"
    )

    plt.xlabel("Ticker")
    plt.ylabel("Return (%)")

    plt.tight_layout()

    plt.savefig(
        OUTPUTS_DIR / "return_chart.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()


def plot_risk_return(summary):
    plt.figure(figsize=(10, 6))

    plt.scatter(
        summary["Volatility (%)"],
        summary["Total Return (%)"]
    )

    for ticker in summary.index:
        plt.annotate(
            ticker,
            (
                summary.loc[
                    ticker,
                    "Volatility (%)"
                ],
                summary.loc[
                    ticker,
                    "Total Return (%)"
                ]
            )
        )

    plt.xlabel("Volatility (%)")
    plt.ylabel("Total Return (%)")

    plt.title(
        "Risk vs Return (2015-2026)"
    )

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        OUTPUTS_DIR / "risk_return_chart.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()