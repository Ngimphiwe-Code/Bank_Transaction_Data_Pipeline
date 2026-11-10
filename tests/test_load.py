
import pandas as pd
from unittest.mock import patch, MagicMock

from src import load


def test_load_data_writes_transactions_table():
    data = pd.DataFrame({
        "amount": [100, 6000],
        "transaction_date": [
            "2026-01-01",
            "2026-01-02"
        ],
        "category": ["Normal", "High Value"]
    })

    mock_engine = MagicMock()
    mock_connection = MagicMock()
    mock_engine.connect.return_value.__enter__.return_value = mock_connection

    with patch("src.load.input", return_value="postgres"), \
         patch("src.load.getpass", return_value="test_password"), \
         patch("src.load.create_engine", return_value=mock_engine), \
         patch.object(data, "to_sql") as mock_to_sql:

        load.load_data(data)

    mock_to_sql.assert_called_once_with(
        name="transactions",
        con=mock_engine,
        if_exists="replace",
        index=False
    )

    mock_engine.dispose.assert_called_once()


def test_load_data_handles_database_failure():
    data = pd.DataFrame({
        "amount": [100],
        "transaction_date": ["2026-01-01"],
        "category": ["Normal"]
    })

    mock_engine = MagicMock()
    mock_connection = MagicMock()
    mock_engine.connect.return_value.__enter__.return_value = mock_connection

    with patch("src.load.input", return_value="postgres"), \
         patch("src.load.getpass", return_value="test_password"), \
         patch("src.load.create_engine", return_value=mock_engine), \
         patch.object(
             data,
             "to_sql",
             side_effect=Exception("Database error")
         ):

        try:
            load.load_data(data)
            assert False, "Expected database error"
        except Exception as error:
            assert str(error) == "Database error"

    mock_engine.dispose.assert_called_once()
