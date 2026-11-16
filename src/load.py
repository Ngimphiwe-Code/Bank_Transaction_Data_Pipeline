

import logging
import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine, URL

# Locate the project folder
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Load credentials from the .env file
load_dotenv(PROJECT_DIR / ".env")

# Configure logging
LOG_DIR = PROJECT_DIR / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=str(LOG_DIR / "pipeline.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True,
)

logger = logging.getLogger(__name__)

def load_data(data):
    """Load cleaned transaction data into PostgreSQL."""

    logger.info("Starting PostgreSQL data load")

    username = os.getenv("DB_USER", "postgres")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST", "localhost")
    port = int(os.getenv("DB_PORT", "5432"))
    database = os.getenv("DB_NAME", "bank_transactions")

    if not password:
        raise ValueError(
            "DB_PASSWORD is missing. Check the .env file in your project folder."
        )

    connection_url = URL.create(
        drivername="postgresql+psycopg2",
        username=username,
        password=password,
        host=host,
        port=port,
        database=database,
    )

    engine = create_engine(connection_url)

    try:
        with engine.connect():
            logger.info("PostgreSQL connection successful")

        rows_loaded = len(data)

        data.to_sql(
            name="transactions",
            con=engine,
            if_exists="replace",
            index=False,
        )

        logger.info("Data loaded successfully")
        logger.info("Rows loaded: %s", rows_loaded)

        print("\nDATA LOADED SUCCESSFULLY!")
        print(f"Rows loaded: {rows_loaded}")
        print("Table created: transactions")

    except Exception:
        logger.exception("PostgreSQL data load failed")
        raise

    finally:
        engine.dispose()