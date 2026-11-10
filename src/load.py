
import logging
from pathlib import Path
from getpass import getpass

from sqlalchemy import create_engine, URL

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


def load_data(data):
    """Load cleaned transaction data into PostgreSQL."""

    logger.info("Starting PostgreSQL data load")

    username = input(
        "PostgreSQL username [postgres]: "
    ).strip() or "postgres"

    password = getpass("Enter your PostgreSQL password: ")

    connection_url = URL.create(
        drivername="postgresql+psycopg2",
        username=username,
        password=password,
        host="localhost",
        port=5432,
        database="bank_transactions"
    )

    engine = create_engine(connection_url)

    try:
        # Test the connection
        with engine.connect():
            logger.info("PostgreSQL connection successful")

        # Load cleaned data into the transactions table
        rows_loaded = len(data)

        data.to_sql(
            name="transactions",
            con=engine,
            if_exists="replace",
            index=False
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

