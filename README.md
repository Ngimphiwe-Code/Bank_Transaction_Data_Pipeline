# Bank Transaction Data Pipeline

A Python-based ETL pipeline that extracts, cleans, validates, and loads bank transaction data into PostgreSQL for analysis.

## Project Overview

This project demonstrates a practical data engineering workflow using Python, pandas, SQLAlchemy, and PostgreSQL. It automates the movement of transaction data from a CSV file into a relational database, while generating data quality reports and pipeline logs.

The project was built to develop practical skills in data processing, database integration, SQL analytics, and version control.

## Architecture

```text
Raw CSV Data
     |
     v
Extract (Python / pandas)
     |
     v
Transform and Clean
     |
     v
Data Quality Checks
     |
     v
Load into PostgreSQL
     |
     v
SQL Analysis and Reporting
```

## Technologies Used

- **Python** — pipeline orchestration and data processing
- **pandas** — data extraction, cleaning, and transformation
- **PostgreSQL** — relational database storage
- **SQLAlchemy** — Python-to-database integration
- **psycopg2** — PostgreSQL database driver
- **SQL** — transaction analysis and aggregation
- **Git and GitHub** — version control and project hosting
- **Logging** — pipeline execution records

## Project Structure

```text
Bank_Transaction_Data_Pipeline/
├── data/
│   └── raw_transactions.csv
├── logs/
│   └── pipeline.log
├── reports/
│   └── data_quality_report.txt
├── sql/
│   └── transaction_analysis.sql
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── data_quality.py
│   └── main.py
├── .gitignore
└── README.md
```

## ETL Process

### 1. Extract
Read transaction records from a CSV file into a pandas DataFrame.

### 2. Transform
Clean and prepare the data by removing duplicate records, validating required columns, converting data types, handling invalid values, and assigning transaction categories based on amount.

### 3. Load
Connect to PostgreSQL and load the processed data into the `transactions` table in the `bank_transactions` database.

### 4. Data Quality and Logging
Generate a data quality report and record pipeline execution information in a log file.

### 5. SQL Analytics
Run SQL queries to calculate transaction statistics and analyse transaction categories.

## Results

The initial test dataset contained 8 transactions.

| Metric | Result |
|---|---:|
| Transactions loaded | 8 |
| Total transaction amount | 23,600 |
| Average transaction amount | 2,950 |
| Minimum transaction amount | 300 |
| Maximum transaction amount | 7,500 |

These results describe the small test dataset used during development; they are not representative of a real bank's transaction volume.

## Key Skills Demonstrated

- Building an end-to-end ETL workflow
- Cleaning and validating structured data
- Connecting Python applications to PostgreSQL
- Writing SQL aggregation queries
- Generating data quality reports
- Implementing application logging
- Managing code with Git and GitHub
- Organising a project into reusable Python modules

## Security

Database credentials are requested at runtime rather than hardcoded in the source code. The `.gitignore` file excludes the raw CSV data and pipeline log from version control.

Never commit database passwords, API keys, private customer information, or other sensitive data to a public repository.

## Future Improvements

- Add automated tests using `pytest`
- Improve data quality checks and validation rules
- Replace table overwriting with incremental loading and duplicate prevention
- Add environment-based database configuration
- Add database constraints and transaction handling
- Introduce automated pipeline scheduling
- Add dashboards for transaction analysis
- Expand testing with a larger, synthetic transaction dataset

## Author

**Ngimphiwe-Code**

GitHub: [View my projects](https://github.com/Ngimphiwe-Code)

---

*This project is an educational portfolio project using sample transaction data. It is not affiliated with or endorsed by any financial institution.
## Running Automated Tests

This project uses pytest to verify data transformation logic.

### Install pytest

```bash
python -m pip install pytest