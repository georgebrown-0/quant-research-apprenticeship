import pandas as pd
import numpy as np

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

def log_returns(prices: pd.Series) -> pd.Series:
    """
    Calculate log returns from a series of prices.

    Parameters:
    prices (pd.Series): A pandas Series of prices.

    Returns:
    pd.Series: A pandas Series of log returns.

    Assumptions:
    - The input prices are in chronological order.
    """
    return np.log((prices / prices.shift(1)).dropna())