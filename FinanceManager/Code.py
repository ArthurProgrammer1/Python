import pandas as pd
from datetime import datetime

try:
    df = pd.read_csv("transactions.csv")
except FileNotFoundError:
    df = pd.DataFrame(columns=["Date", "Category", "Type", "Amount"])

def add_transaction(date, category, trans_type, amount):
    """
    Adds a new transaction to the DataFrame and saves it to a CSV file.

    Parameters:
    - date (str): The date of the transaction.
    - category (str): The category of the transaction (e.g., Food, Rent).
    - trans_type (str): The type of the transaction (e.g., Income, Expense).
    - amount (float): The amount of the transaction.
    """
    global df
    new_row = pd.DataFrame([[date, category, trans_type, amount]], columns=df.columns)
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv("transactions.csv", index=False)
    print("Transaction added successfully!")


def view_balance():
    """
    Calculates and prints the current balance based on transactions.

    Returns:
    - balance (float): The current balance calculated from all transactions.
    """
    global df
    income = df[df["Type"] == "Income"]["Amount"].sum()
    expense = df[df["Type"] == "Expense"]["Amount"].sum()
    balance = income - expense
    print(f"Current balance: ${balance:.2f}")
    return balance

def display_transactions():
    """
    Displays all transactions stored in the DataFrame.
    """
    global df
    print(f"All Transactions: {df}")

def filter_transactions_by_date(start_date, end_date):
    """
    Filters and displays transactions within a given date range.

    Parameters:
    - start_date (str): The start date in YYYY-MM-DD format.
    - end_date (str): The end date in YYYY-MM-DD format.
    """
    global df
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    df["Date"] = pd.to_datetime(df["Date"])
    filtered_df = df[(df["Date"] >= start) & (df["Date"] <= end)]

    print(f"Transactions from {start_date} to {end_date}:")
    print(filtered_df)

def main():
    """
    The main function to run the script. It provides a menu for the user to select different actions.
    """
    while True:
        print("\nMenu:")
        print("1. Add a new transaction")
        print("2. View current balance")
        print("3. Display all transactions")
        print("4. Filter transactions by date range")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD): ")
            category = input("Enter the category (e.g., Food, Rent): ")
            trans_type = input("Enter the type (Income/Expense): ")
            try:
                amount = float(input("Enter the amount: "))
                add_transaction(date, category, trans_type, amount)
            except ValueError:
                print("Invalid input for amount. Please enter a number.")
        elif choice == '2':
            view_balance()
        elif choice == '3':
            display_transactions()
        elif choice == '4':
            start_date = input("Enter the start date (YYYY-MM-DD): ")
            end_date = input("Enter the end date (YYYY-MM-DD): ")
            filter_transactions_by_date(start_date, end_date)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select an option from the menu.")

if __name__ == "__main__":
    main()
