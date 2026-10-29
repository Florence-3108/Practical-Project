import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


class LibraryDashboard:

    def __init__(self):
        self.data = None

    def load_data(self, file_path):
        try:
            if not os.path.exists(file_path):
                print("Error: CSV file not found!")
                return

            if not file_path.endswith(".csv"):
                print("Please select a CSV file.")
                return

            self.data = pd.read_csv(file_path)

            required_columns = [
                "Transaction ID", "Date", "User ID",
                "Book Title", "Genre", "Borrowing Duration (Days)"
            ]

            for column in required_columns:
                if column not in self.data.columns:
                    print("Missing column:", column)
                    self.data = None
                    return

            self.data.drop_duplicates(inplace=True)
            self.data.dropna(subset=required_columns, inplace=True)

            self.data["Date"] = pd.to_datetime(
                self.data["Date"], errors="coerce"
            )

            self.data["Borrowing Duration (Days)"] = pd.to_numeric(
                self.data["Borrowing Duration (Days)"],
                errors="coerce"
            )

            self.data.dropna(
                subset=["Date", "Borrowing Duration (Days)"],
                inplace=True
            )

            self.data = self.data[
                self.data["Borrowing Duration (Days)"] >= 0
            ]

            if self.data.empty:
                print("No valid data found!")
                return

            self.data["Month"] = self.data["Date"].dt.to_period("M").astype(str)
            self.data["Day"] = self.data["Date"].dt.day_name()

            print("\nDataset loaded successfully!")
            print(self.data.head())

        except Exception as e:
            print("Error loading file:", e)

    def calculate_statistics(self):
        if self.data is None:
            print("Please load the dataset first.")
            return

        duration = self.data["Borrowing Duration (Days)"].to_numpy()

        popular_book = self.data["Book Title"].mode()[0]
        average_duration = np.mean(duration)
        standard_deviation = np.std(duration)

        busiest_day = self.data["Day"].mode()[0]

        print("\n--- LIBRARY STATISTICS ---")
        print("Total transactions:", len(self.data))
        print("Most borrowed book:", popular_book)
        print("Average borrowing duration:", round(average_duration, 2), "days")
        print("Standard deviation:", round(standard_deviation, 2))
        print("Busiest day:", busiest_day)

        print("\nBorrowings by genre:")
        print(self.data["Genre"].value_counts())

        print("\nTop 5 most borrowed books:")
        print(self.data["Book Title"].value_counts().head(5))

    def filter_transactions(self, condition=None):
        if self.data is None:
            print("Please load the dataset first.")
            return

        print("\n1. Filter by genre")
        print("2. Filter by minimum borrowing duration")
        print("3. Filter by date range")

        choice = input("Enter your choice: ")

        if choice == "1":
            genre = input("Enter genre: ")
            result = self.data[
                self.data["Genre"].str.lower() == genre.lower()
            ]

        elif choice == "2":
            try:
                days = float(input("Enter minimum days: "))
                result = self.data[
                    self.data["Borrowing Duration (Days)"] >= days
                ]
            except ValueError:
                print("Please enter a valid number.")
                return

        elif choice == "3":
            try:
                start = pd.to_datetime(input("Enter start date (YYYY-MM-DD): "))
                end = pd.to_datetime(input("Enter end date (YYYY-MM-DD): "))

                if start > end:
                    print("Start date must be before end date.")
                    return

                result = self.data[
                    (self.data["Date"] >= start) &
                    (self.data["Date"] <= end)
                ]
            except ValueError:
                print("Invalid date format.")
                return

        else:
            print("Invalid choice!")
            return

        print("\nFiltered transactions:")
        if result.empty:
            print("No matching records found.")
        else:
            print(result.to_string(index=False))

    def generate_report(self):
        if self.data is None:
            print("Please load the dataset first.")
            return

        plt.figure(figsize=(8, 5))
        self.data["Book Title"].value_counts().head(5).plot(
            kind="bar", color="skyblue"
        )
        plt.title("Top 5 Most Borrowed Books")
        plt.xlabel("Book Title")
        plt.ylabel("Number of Borrowings")
        plt.xticks(rotation=30, ha="right")
        plt.tight_layout()
        plt.show()

        monthly = self.data.groupby("Month").size()

        plt.figure(figsize=(8, 5))
        monthly.plot(kind="line", marker="o")
        plt.title("Monthly Borrowing Trends")
        plt.xlabel("Month")
        plt.ylabel("Number of Borrowings")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        plt.figure(figsize=(7, 7))
        self.data["Genre"].value_counts().plot(
            kind="pie", autopct="%1.1f%%"
        )
        plt.title("Books Borrowed by Genre")
        plt.ylabel("")
        plt.tight_layout()
        plt.show()

        heatmap_data = self.data.pivot_table(
            index="Day",
            columns="Month",
            values="Transaction ID",
            aggfunc="count",
            fill_value=0
        )

        days = [
            "Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"
        ]
        heatmap_data = heatmap_data.reindex(days, fill_value=0)

        plt.figure(figsize=(10, 5))
        sns.heatmap(heatmap_data, annot=True, fmt="g", cmap="Blues")
        plt.title("Borrowing Activity by Day and Month")
        plt.xlabel("Month")
        plt.ylabel("Day of Week")
        plt.tight_layout()
        plt.show()

    def summary_report(self):
        if self.data is None:
            print("Please load the dataset first.")
            return

        print("\n===== E-LIBRARY SUMMARY REPORT =====")
        print("Total transactions:", len(self.data))
        print("Unique users:", self.data["User ID"].nunique())
        print("Unique books:", self.data["Book Title"].nunique())
        print("Number of genres:", self.data["Genre"].nunique())
        print(
            "Average borrowing duration:",
            round(self.data["Borrowing Duration (Days)"].mean(), 2),
            "days"
        )
        print("====================================")


dashboard = LibraryDashboard()

while True:
    print("\n===== E-LIBRARY DATA INSIGHTS DASHBOARD =====")
    print("1. Load Dataset")
    print("2. Calculate Statistics")
    print("3. Filter Transactions")
    print("4. Generate Visualizations")
    print("5. Generate Summary Report")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        file_path = input("Enter CSV file path: ")
        dashboard.load_data(file_path)

    elif choice == "2":
        dashboard.calculate_statistics()

    elif choice == "3":
        dashboard.filter_transactions()

    elif choice == "4":
        dashboard.generate_report()

    elif choice == "5":
        dashboard.summary_report()

    elif choice == "6":
        print("Thank you for using the Library Dashboard!")
        break

    else:
        print("Invalid choice! Please try again.")
