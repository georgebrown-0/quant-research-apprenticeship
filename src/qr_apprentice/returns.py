import pandas as pd


def simple_returns(prices: pd.Series) -> pd.Series:
    """
    Calculate simple returns from a series of prices.

    Parameters:
    prices (pd.Series): A pandas Series of prices.

    Returns:
    pd.Series: A pandas Series of simple returns.

    Assumptions:
    - The input prices are in chronological order.
    """
    return prices.pct_change().dropna()