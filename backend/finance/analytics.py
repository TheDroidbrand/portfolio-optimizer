import yfinance as yf # type: ignore
import pandas as pd # type: ignore
import numpy as np

def calculate_metrics(ticker, period="1y"):
    data = yf.Ticker(ticker).history(period=period)

    prices = data["Close"]

    daily_returns = prices.pct_change().dropna()