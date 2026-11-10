
import logging
from pathlib import Path

from extract import extract_data
from transform import transform_data
from load import load_data
from data_quality import generate_report


# Locate the project folder
PROJECT_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = PROJECT_DIR / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=str(LOG_DIR / "pipeline.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

logger = logging.getLogger(__name__)


def main():
    try:
        logger.info("BANK TRANSACTION PIPELINE STARTED")
        print("BANK TRANSACTION PIPELINE STARTED")

        # Stage 1: Extract
        raw_data = extract_data()

        # Stage 2: Transform
        cleaned_data = transform_data(raw_data)

        # Stage 3: Load into PostgreSQL
        load_data(cleaned_data)

        # Stage 4: Generate data quality report
        generate_report(
            raw_data=raw_data,
            clean_data=cleaned_data,
            rows_loaded=len(cleaned_data)
        )

        logger.info("PIPELINE COMPLETED SUCCESSFULLY")
        print("\nETL PIPELINE COMPLETED SUCCESSFULLY!")

    except Exception:
        logger.exception("ETL PIPELINE FAILED")
        print("\nPipeline failed. Check logs/pipeline.log.")
        raise


if __name__ == "__main__":
    main()

