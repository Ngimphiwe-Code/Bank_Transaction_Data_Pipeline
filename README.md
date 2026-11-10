# Bank Transaction Data Pipeline

## Project Overview

This project is an end-to-end Data Engineering pipeline built with Python and PostgreSQL. It extracts bank transaction data from a CSV file, cleans and transforms the data, loads it into a PostgreSQL database, and generates a data quality report.

The project demonstrates essential Data Engineering skills, including ETL development, data cleaning, database integration, SQL analytics, logging, and data quality monitoring.

## Project Objectives

- Build an automated ETL pipeline.
- Extract transaction data from a CSV file.
- Clean and transform transaction records using Python.
- Load processed data into PostgreSQL.
- Generate data quality reports.
- Analyse transactions using SQL.
- Record pipeline activities and errors using logging.

## Technologies Used

- **Python** — ETL development and data processing.
- **Pandas** — Data cleaning and transformation.
- **PostgreSQL** — Relational database storage.
- **SQL** — Transaction analysis and reporting.
- **SQLAlchemy** — Python-to-database connectivity.
- **Psycopg2** — PostgreSQL database driver.
- **Logging** — Pipeline activity tracking.
- **VS Code** — Development environment.

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
│   ├── main.py
│   └── data_quality.py
└── README.md
```

## ETL Process

### 1. Extract
Read raw bank transaction records from a CSV file using Pandas.

### 2. Transform
Clean the data by removing duplicate records, validating required fields, converting transaction amounts to numeric values, converting dates to datetime values, and assigning transaction categories.

### 3. Load
Load the cleaned transaction data into a PostgreSQL table named `transactions`.

### 4. Data Quality
Generate a report containing record counts, duplicate information, missing-value statistics, and the number of records loaded.

### 5. SQL Analytics
Use SQL queries to calculate transaction counts, total amounts, average amounts, minimum values, and maximum values.

## Initial Results

The pipeline was successfully executed against the current sample dataset.

| Metric | Result |
|---|---:|
| Transactions loaded | 8 |
| Total transaction amount | 23,600 |
| Average transaction amount | 2,950 |
| Smallest transaction | 300 |
| Largest transaction | 7,500 |

These results describe the current sample dataset and may change when new data is loaded.

## Key Skills Demonstrated

- ETL pipeline development
- Data cleaning and validation
- Python programming
- PostgreSQL integration
- SQL aggregation and analysis
- Data quality reporting
- Logging and pipeline monitoring
- Project organisation and documentation

## Future Improvements

- Automate pipeline execution.
- Add more robust exception handling and database transactions.
- Use environment variables to protect database credentials.
- Add automated tests for data quality.
- Introduce larger datasets and more advanced SQL analytics.
- Publish the project on GitHub.

## Author

Computer Science and Mathematics student developing practical Data Engineering skills through hands-on projects.