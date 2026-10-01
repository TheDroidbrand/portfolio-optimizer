from pydantic import BaseModel, model_validator
from typing import List


class PortfolioRequest(BaseModel):
    tickers: List[str]
    weights: List[float]

    @model_validator(mode="after")
    def validate_weights(self):

        if len(self.tickers) != len(self.weights):
            raise ValueError(
                "Tickers and weights must match"
            )

        if round(sum(self.weights), 5) != 1:
            raise ValueError(
                "Weights must sum to 1"
            )

        return self


class OptimizationRequest(BaseModel):
    tickers: List[str]