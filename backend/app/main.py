from fastapi import FastAPI

from finance.data_fetcher import get_stock_data

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