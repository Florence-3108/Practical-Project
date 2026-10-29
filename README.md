# E-Library Data Insights Dashboard

## Project Description
The E-Library Data Insights Dashboard is a Python-based project used to analyze library book borrowing data. It provides information about popular books, borrowing duration, library usage, and borrowing trends over time.

## Features
- Load and validate CSV datasets.
- Remove duplicate and missing records.
- Calculate library statistics using NumPy and Pandas.
- Find the most borrowed book and average borrowing duration.
- Filter transactions by genre, date range, and borrowing duration.
- Generate bar charts, line graphs, pie charts, and heatmaps.
- Generate a summary report of library transactions.
- Handle invalid inputs and file errors.

## Technologies Used
- **Python** – Main programming language.
- **Pandas** – Data cleaning and analysis.
- **NumPy** – Numerical calculations.
- **Matplotlib** – Data visualization.
- **Seaborn** – Heatmap visualization.

## Project Files
```text
E-Library-Data-Insights/
│
├── library_dashboard.py
├── library_transactions.csv
└── README.md
```

## Dataset Details
The `library_transactions.csv` file contains the following columns:

- **Transaction ID:** Unique transaction identifier.
- **Date:** Date of the borrowing transaction.
- **User ID:** Unique library user identifier.
- **Book Title:** Name of the borrowed book.
- **Genre:** Category of the book.
- **Borrowing Duration (Days):** Number of days the book was borrowed.

## Installation

Install the required Python libraries by running:

```bash
pip install pandas numpy matplotlib seaborn
```

## How to Run
1. Download or clone the project repository.
2. Keep the Python file and CSV dataset in the same folder.
3. Open the folder in VS Code.
4. Open the terminal.
5. Run the following command:

```bash
python library_dashboard.py
```

6. Select option `1` to load the dataset.
7. Enter the CSV file path:

```text
library_transactions.csv
```

8. Use the menu options to calculate statistics, filter transactions, generate visualizations, and view the summary report.

## Menu Options
1. Load Dataset
2. Calculate Statistics
3. Filter Transactions
4. Generate Visualizations
5. Generate Summary Report
6. Exit

## Expected Output
The program displays library statistics, including the most borrowed book, average borrowing duration, busiest day, total transactions, and unique users. It also generates visualizations to help understand book popularity, genre distribution, and monthly borrowing trends.

## Concepts Used
- Object-Oriented Programming (OOP)
- Classes and objects
- Conditional statements and loops
- Exception handling
- NumPy arrays
- Pandas DataFrames
- Data cleaning and filtering
- Data visualization

## Conclusion
This project demonstrates how Python libraries can be used to analyze library transactions and visualize useful information. It helps understand borrowing patterns and supports better library management.