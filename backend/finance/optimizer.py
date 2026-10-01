import yfinance as yf
import pandas as pd
import numpy as np


def generate_efficient_frontier(
    tickers,
    num_portfolios=10000,
    period="1y"
):

    data = yf.download(
        tickers,
        period=period,
        auto_adjust=True
    )["Close"]

    returns = data.pct_change().dropna()

    mean_returns = returns.mean() * 252

    covariance_matrix = returns.cov() * 252

    risk_free_rate = 0.02

    portfolio_results = []

    for _ in range(num_portfolios):

        weights = np.random.random(
            len(tickers)
        )

        weights /= np.sum(weights)

        portfolio_return = np.sum(
            mean_returns * weights
        )

        portfolio_volatility = np.sqrt(
            np.dot(
                weights,
                np.dot(
                    covariance_matrix,
                    weights
                )
            )
        )

        sharpe_ratio = (
            portfolio_return
            - risk_free_rate
        ) / portfolio_volatility

        portfolio_results.append(
            {
                "return": float(
                    portfolio_return
                ),
                "risk": float(
                    portfolio_volatility
                ),
                "sharpe": float(
                    sharpe_ratio
                ),
                "weights": weights.tolist()
            }
        )

    return portfolio_results