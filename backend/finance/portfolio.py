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