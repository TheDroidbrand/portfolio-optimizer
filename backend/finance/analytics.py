import yfinance as yf # type: ignore
import pandas as pd # type: ignore
import numpy as np

def calculate_metrics(ticker, period="1y"):
    data = yf.Ticker(ticker).history(period=period)

    prices = data["Close"]

    daily_returns = prices.pct_change().dropna()

    annual_return = daily_returns.mean() * 252

    annual_volatility = daily_returns.std() * np.sqrt(252)

    risk_free_rate = 0.02

    sharpe_ratio = (
        annual_return - risk_free_rate
    ) / annual_volatility