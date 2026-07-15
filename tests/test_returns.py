import pandas as pd

from qr_apprentice.returns import simple_returns


def test_simple_returns_calculates_expected_values() -> None:
    prices = pd.Series([100.0, 110.0, 99.0])

    result = simple_returns(prices)

    expected = pd.Series([0.10, -0.10], index=[1, 2])

    pd.testing.assert_series_equal(result, expected)