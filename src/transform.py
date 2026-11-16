import pandas as pd
from pathlib import Path
def transform_data(data):
    """Clean and transform transaction data."""

    required_columns = {
    "transaction_id",
    "amount",
    "transaction_date",
}
    missing_columns = required_columns - set(data.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    # Remove duplicate rows
    data = data.drop_duplicates().copy()

    # Remove rows with missing values
    data = data.dropna().copy()

    # Convert transaction dates
    data["transaction_date"] = pd.to_datetime(
        data["transaction_date"],
        errors="coerce"
    )

    # Remove rows with invalid dates
    data = data.dropna(subset=["transaction_date"]).copy()

    # Create a transaction category
    data["category"] = data["amount"].apply(
        lambda amount: "High Value" if amount > 5000 else "Normal"
    )

    return data


def main():
    # Locate the project folder
    project_folder = Path(__file__).resolve().parent.parent

    # Locate the raw transaction file
    file_path = project_folder / "data" / "raw_transactions.csv"

    # Read the raw data
    data = pd.read_csv(file_path)

    print("BEFORE CLEANING:")
    print(data.isnull().sum())
    print("Duplicate rows:", data.duplicated().sum())

    # Transform the data
    cleaned_data = transform_data(data)

    print("\nAFTER CLEANING:")
    print(cleaned_data)

    print("\nCleaned dataset shape:")
    print(cleaned_data.shape)


if __name__ == "__main__":
    main()
