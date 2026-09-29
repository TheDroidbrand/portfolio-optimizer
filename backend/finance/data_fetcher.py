import yfinance as yf

def get_stock_data(ticker, period="1y"):
    stock = yf.Ticker(ticker)

    data = stock.history(period=period)

    return data.reset_index().to_dict(orient="records")