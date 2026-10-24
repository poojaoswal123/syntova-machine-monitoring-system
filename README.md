# syntova-machine-monitoring-system
Machine Power Monitoring and Energy Estimation using Python and MySQL.
# Machine Monitoring System

## Project Overview
This project monitors machine power readings using Python and MySQL. It checks whether the power usage exceeds the configured limit and calculates estimated energy consumption.

## Technologies Used
- Python
- SQL

## Features
- Checks machine power readings against configured limits.
- Identifies HIGH and NORMAL power readings.
- Calculates estimated energy consumption in kWh.
- Calculates total energy, average power, and peak power for each machine.
- Counts readings that exceed the power limit.
- Generates daily machine power summaries using SQL.
- Identifies readings that exceed the configured power limit.

## Energy Calculation
Each reading represents 15 minutes.

**Energy (kWh) = Power (kW) × 0.25**

## Project Files
- `Machine_monitoring_python_code.py` – Python program for power monitoring and energy estimation.
- `Machine_monitoring_sql.sql` – MySQL tables, sample data, and SQL queries.
- `Machine_Monitoring_documentation.pdf` – Problem understanding, assumptions, algorithm, logic, testing, and complexity analysis.

## Purpose
This project was completed as part of the Syntova Fresher Assessment to practise Python programming, SQL queries, data validation, calculations, and problem-solving.
