
import pandas as pd
import logging
from pathlib import Path

# Locate the project folder
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Locate the raw transaction file
DATA_FILE = PROJECT_DIR / "data" / "raw_transactions.csv"

# Set up logging
LOG_DIR = PROJECT_DIR / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=str(LOG_DIR / "pipeline.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

logger = logging.getLogger(__name__)


def extract_data():
    """Read raw transaction data from the CSV file."""

    logger.info("Starting data extraction")

    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Transaction file not found: {DATA_FILE}"
        )

    data = pd.read_csv(DATA_FILE)

    logger.info("Data extraction successful")
    logger.info("Rows extracted: %s", len(data))
    logger.info("Columns: %s", data.columns.tolist())

    print("TRANSACTION DATA EXTRACTED SUCCESSFULLY!")
    print(data.head())

    print("\nDataset shape:")
    print(data.shape)

    print("\nColumn names:")
    print(data.columns.tolist())

    return data


if __name__ == "__main__":
    extract_data()

