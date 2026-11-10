
import pandas as pd

from src.transform import transform_data


def test_remove_duplicates():
    data = pd.DataFrame({
        "amount": [100, 100, 6000],
        "transaction_date": [
            "2026-01-01",
            "2026-01-01",
            "2026-01-02"
        ]
    })

    result = transform_data(data)

    assert len(result) == 2


def test_remove_invalid_values():
    data = pd.DataFrame({
        "amount": [100, "invalid", 300],
        "transaction_date": [
            "2026-01-01",
            "invalid-date",
            "2026-01-03"
        ]
    })

    result = transform_data(data)

    assert len(result) == 2


def test_transaction_category():
    data = pd.DataFrame({
        "amount": [2000, 6000],
        "transaction_date": [
            "2026-01-01",
            "2026-01-02"
        ]
    })

    result = transform_data(data)

    assert result.loc[0, "category"] == "Normal"
    assert result.loc[1, "category"] == "High Value"


def test_missing_columns():
    data = pd.DataFrame({
        "amount": [100, 200]
    })

    try:
        transform_data(data)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for missing columns"


def test_original_data_is_unchanged():
    data = pd.DataFrame({
        "amount": [100, 6000],
        "transaction_date": [
            "2026-01-01",
            "2026-01-02"
        ]
    })

    original_data = data.copy(deep=True)

    transform_data(data)

    pd.testing.assert_frame_equal(data, original_data)


def test_amount_of_5000_is_normal():
    data = pd.DataFrame({
        "amount": [5000],
        "transaction_date": ["2026-01-01"]
    })

    result = transform_data(data)

    assert result.iloc[0]["category"] == "Normal"
