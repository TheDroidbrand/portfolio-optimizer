from fastapi import FastAPI # type: ignore

from finance.data_fetcher import get_stock_data
from finance.analytics import calculate_metrics

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