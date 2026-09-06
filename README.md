# Automated Data Processing & Report Generator

A lightweight Python automation tool designed to process raw operational logs (`.csv`), aggregate key performance metrics, and automatically export structured text reports (`.txt`) for executive review.

## Overview
Many operational teams spend significant time manually organizing spreadsheet data and writing daily summary reports. This tool automates the ingestion, calculation, and reporting workflow, reducing manual processing time and eliminating data entry errors.

## Key Features
- **CSV Data Ingestion:** Automatically reads and parses raw CSV log files containing operational and ticket data.
- **Metric Computation:** Calculates total log volume, resolved task counts, and task resolution percentages.
- **Category Breakdown:** Aggregates operational tickets by department/category (e.g., Network, Hardware, Software, Finance Sync) to identify process bottlenecks.
- **Automated Text Reporting:** Generates timestamped summary reports (`daily_report.txt`) formatted for management decision-making.

## Tech Stack
- **Language:** Python 3
- **Libraries Used:** Standard Library (`csv`, `datetime`)

## Project Structure
```text
data-report-generator/
│
├── logs.csv           # Input file containing raw operational log data
├── main.py            # Main Python automation script
├── daily_report.txt   # Output file generated automatically by the script
└── README.md          # Project documentation
