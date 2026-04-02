# Student Exam Score Analysis

## Project Overview

This project analyzes a student dataset to determine **what factors affect exam scores**. Using **Python**, **pandas**, **NumPy**, and **SQLite**, the pipeline loads raw CSV data, cleans it, stores it in a SQL database, performs SQL queries for subset extraction, and conducts statistical analysis to identify key predictors of academic performance.

The goal is to demonstrate an industry‑standard data analysis workflow that combines the strengths of pandas (data wrangling), SQL (querying/aggregation), and NumPy (numerical operations).

---

## Dataset

The dataset contains **6,607 student records** with 11 columns:

| Column Name                    | Type      | Description                                      |
|--------------------------------|-----------|--------------------------------------------------|
| `Hours_Studied`                | float     | Weekly study hours (1.1 – 44.0)                 |
| `Attendance`                   | float     | Attendance percentage (60 – 100)                |
| `Parental_Involvement`         | text      | Low / Medium / High                             |
| `Access_to_Resources`          | text      | Low / Medium / High                             |
| `Extracurricular_Activities`   | text      | Yes / No                                        |
| `Sleep_Hours`                  | float     | Daily sleep hours (4 – 10)                      |
| `Previous_Scores`              | float     | Score from previous assessment (50 – 100)       |
| `Motivation_Level`             | text      | Low / Medium / High                             |
| `Internet_Access`              | text      | Yes / No                                        |
| `Tutoring_Sessions`            | integer   | Number of tutoring sessions (0 – 8)             |
| `Final_Exam_Score`             | float     | Target variable (29.7 – 95.2)                   |

No missing values were found. Outliers in `Hours_Studied` (up to 44) were examined and retained as plausible for weekly study hours.

---

## Tools & Libraries

- **Python 3.8+**
- **pandas** – data cleaning and manipulation
- **NumPy** – numerical operations and correlations
- **SQLite3** – embedded database for SQL queries


---

## Project Workflow

1. **Load** – Read CSV into pandas DataFrame.
2. **Clean** – Handle missing values (none), standardise categorical text, remove impossible values, inspect outliers.
3. **Store** – Save cleaned DataFrame to SQLite database using `.to_sql()`.
4. **Transform** – Use SQL queries to pull specific subsets (e.g., students with >30 study hours, grouped by motivation level).
5. **Analyze** – Perform correlation, group comparisons, and performance classification using pandas and numpy.
6. **Report** – Summarise findings and actionable insights.

---

##Folder Structure

├── .gitignore
├── LICENSE
├── README.md
│
├── student-data-analysis/
    ├── Analysis_Data.txt
    ├── Analysis_Report.txt
    ├── student_data.db
    ├── student_data_analysis.py
    └── student_dataset.csv
