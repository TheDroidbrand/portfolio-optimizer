from fastapi import FastAPI # type: ignore

from finance.data_fetcher import get_stock_data
from finance.analytics import calculate_metrics
from app.schemas import PortfolioRequest
from finance.portfolio import (
    calculate_portfolio_metrics
)

app = FastAPI(
    title="Portfolio Optimizer API"
)

@app.get("/")
def root():
    return {
        "message": "Portfolio Optimizer API Running"
    }

@app.get("/stock/{ticker}")
def stock_data(ticker: str):
    return get_stock_data(ticker.upper())

@app.get("/analytics/{ticker}")
def analytics(ticker: str):
    return calculate_metrics(ticker.upper())

@app.post("/portfolio")
def portfolio_analysis(
    request: PortfolioRequest
):
    return calculate_portfolio_metrics(
        request.tickers,
        request.weights
    )