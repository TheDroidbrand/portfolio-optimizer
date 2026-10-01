from pydantic import BaseModel
from typing import List


class PortfolioRequest(BaseModel):
    tickers: List[str]
    weights: List[float]