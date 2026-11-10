
from pathlib import Path
from datetime import datetime
import logging

PROJECT_DIR = Path(__file__).resolve().parent.parent
REPORT_DIR = PROJECT_DIR / "reports"
REPORT_DIR.mkdir(parents=True, exist_ok=True)

logger = logging.getLogger(__name__)


def generate_report(raw_data, clean_data, rows_loaded):
    """Generate a data quality report for the current pipeline run."""

    report_path = REPORT_DIR / "data_quality_report.txt"

    duplicates = int(raw_data.duplicated().sum())
    missing_values = raw_data.isnull().sum()
    missing_total = int(missing_values.sum())

    report_lines = [
        "BANK TRANSACTION DATA QUALITY REPORT",
        "=" * 40,
        f"Report generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        f"Rows extracted: {len(raw_data)}",
        f"Duplicate rows detected: {duplicates}",
        f"Rows after cleaning: {len(clean_data)}",
        f"Missing values detected: {missing_total}",
        f"Rows loaded into PostgreSQL: {rows_loaded}",
        "",
        "Missing values by column:",
    ]

    for column, count in missing_values.items():
        report_lines.append(f"{column}: {count}")

    report_lines.extend([
        "",
        "PIPELINE STATUS: SUCCESSFUL",
    ])
git add .
    report_path.write_text(
        "\n".join(report_lines) + "\n",
        encoding="utf-8"
    )

    logger.info("Data quality report generated: %s", report_path)
    print(f"\nData quality report created: {report_path}")

    return report_path

