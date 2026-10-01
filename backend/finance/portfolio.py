import yfinance as yf
import pandas as pd
import numpy as np


def calculate_portfolio_metrics(
    tickers,
    weights,
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

    risk_free_rate = 0.02

    sharpe_ratio = (
        portfolio_return - risk_free_rate
    ) / portfolio_volatility

    return {
        "portfolio_return": round(
            float(portfolio_return),
            4
        ),
        "portfolio_volatility": round(
            float(portfolio_volatility),
            4
        ),
        "portfolio_sharpe_ratio": round(
            float(sharpe_ratio),
            4
        ),
    }