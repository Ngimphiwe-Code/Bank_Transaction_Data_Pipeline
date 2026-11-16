# Bank Transaction Data Pipeline

A Python-based ETL pipeline that extracts, cleans, validates, and loads bank transaction data into PostgreSQL for analysis.

## Project Overview

This project demonstrates a practical data engineering workflow using Python, pandas, SQLAlchemy, and PostgreSQL. It automates the movement of transaction data from a CSV file into a relational database, generates data quality reports, and records pipeline execution information through logging.

The project was built to develop practical skills in data processing, database integration, SQL analytics, automated testing, and version control.

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
- **pytest** — automated testing
- **Git and GitHub** — version control and project hosting
- **GitHub Actions** — continuous integration and automated test execution
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
├── tests/
│   ├── test_load.py
│   └── test_transform.py
├── .github/
│   └── workflows/
├── .gitignore
├── requirements.txt
└── README.md
```

## ETL Process

### 1. Extract

Read transaction records from a CSV file into a pandas DataFrame.

### 2. Transform

Clean and prepare the data by removing duplicate records, validating required columns, converting data types, handling missing or invalid values, and assigning transaction categories based on transaction amount.

### 3. Load

Connect to PostgreSQL and load the processed data into the `transactions` table in the `bank_transactions` database.

The pipeline uses table replacement for its current loading workflow. Incremental loading and database-level duplicate prevention are potential future improvements.

### 4. Data Quality and Logging

Generate a data quality report containing transaction statistics and record pipeline execution information in a log file.

### 5. SQL Analytics

Use SQL queries to calculate transaction statistics, including record counts, total amounts, averages, minimums, and maximums.

## Results

The test dataset contained eight unique transactions after cleaning and loading.

| Metric | Result |
|---|---:|
| Transactions loaded | 8 |
| Total transaction amount | 23,600 |
| Average transaction amount | 2,950 |
| Minimum transaction amount | 300 |
| Maximum transaction amount | 7,500 |

These results describe a small sample dataset used during development. They are not representative of a real bank's transaction volume.

## Automated Testing and Continuous Integration

The project uses `pytest` to test data transformation and database-loading behaviour.

The test suite contains eight automated tests covering transformation rules and loading behaviour. All eight tests passed during local verification.

GitHub Actions is configured to run automated tests when changes are pushed to the repository. The workflow has also completed successfully.

### Run the tests locally

Install the project dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the automated tests:

```bash
python -m pytest -v
```

## Running the Pipeline

### Prerequisites

- Python installed
- PostgreSQL installed and running
- A PostgreSQL database named `bank_transactions`
- The required database connection settings
- The sample CSV file in the expected project location

### Execute the pipeline

From the project root directory, run:

```bash
python -m src.main
```

The pipeline extracts, transforms, and loads the transaction data, generates a data quality report, and records execution information.

Ensure that PostgreSQL is running and that your database connection settings are correct before executing the pipeline.

## Key Skills Demonstrated

- Building an end-to-end ETL workflow
- Cleaning and validating structured data
- Connecting Python applications to PostgreSQL
- Writing SQL aggregation queries
- Generating data quality reports
- Implementing application logging
- Writing and running automated tests
- Configuring continuous integration with GitHub Actions
- Organising a project into reusable Python modules
- Managing code with Git and GitHub

## Security

Database credentials are requested at runtime rather than hardcoded in the source code.

The `.gitignore` file is intended to exclude raw data and pipeline logs from version control where configured. Database passwords, API keys, private customer information, and other sensitive data must never be committed to a public repository.

## Future Improvements

- Implement incremental loading and database-level duplicate prevention
- Improve data quality checks and validation rules
- Add environment-based database configuration
- Introduce database constraints and transaction handling
- Add automated pipeline scheduling
- Develop dashboards for transaction analysis
- Expand testing with a larger synthetic transaction dataset

## Author

**Ngimphiwe-Code**

GitHub: [View my projects](https://github.com/Ngimphiwe-Code)

---

*This project is an educational portfolio project using sample transaction data. It is not affiliated with or endorsed by any financial institution.*
