
import logging
from pathlib import Path

import pandas as pd

# Locate the project folder
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Configure logging
LOG_DIR = PROJECT_DIR / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=str(LOG_DIR / "pipeline.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

logger = logging.getLogger(__name__)


def transform_data(data):
    """Clean and transform the extracted transaction data."""

    logger.info("Starting data transformation")

    # Work on a copy of the original data
    data = data.copy()

    print("BEFORE CLEANING:")
    print(data.isnull().sum())
    print("Duplicate rows:", data.duplicated().sum())

    # 1. Remove duplicate rows
    original_rows = len(data)
    data = data.drop_duplicates().copy()
    duplicates_removed = original_rows - len(data)

    # 2. Check required columns
    required_columns = ["amount", "transaction_date"]

    missing_columns = [
        column for column in required_columns
        if column not in data.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    # 3. Convert transaction amounts to numeric values
    data["amount"] = pd.to_numeric(
        data["amount"],
        errors="coerce"
    )

    # 4. Convert transaction dates
    data["transaction_date"] = pd.to_datetime(
        data["transaction_date"],
        errors="coerce"
    )

    # 5. Remove rows with missing or invalid required values
    before_validation = len(data)

    data = data.dropna(
        subset=["amount", "transaction_date"]
    ).copy()

    invalid_rows_removed = before_validation - len(data)

    # 6. Create a transaction category
    data["category"] = data["amount"].apply(
        lambda amount: "High Value" if amount > 5000 else "Normal"
    )

    logger.info("Data transformation completed")
    logger.info("Duplicate rows removed: %s", duplicates_removed)
    logger.info("Invalid rows removed: %s", invalid_rows_removed)
    logger.info("Rows after cleaning: %s", len(data))

    print("\nAFTER CLEANING:")
    print(data)

    print("\nCleaned dataset shape:")
    print(data.shape)

    print("\nDuplicate rows removed:", duplicates_removed)
    print("Invalid rows removed:", invalid_rows_removed)

    return data


if __name__ == "__main__":
    # Allow this file to be tested independently
    from extract import extract_data

    raw_data = extract_data()
    cleaned_data = transform_data(raw_data)
