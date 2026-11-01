import datetime as dt
import expense_utils
from report_utils import monthly_report
import os
import math

expenses = []
print("===== EXPENSE TRACKER =====")
while True:
    description = input("\nEnter description: ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    if not expense_utils.validate_amount(amount):
        print("Invalid amount!")
        continue

    date = input("Enter date (YYYY-MM-DD), blank for today: ")
    if date == "":
        date = dt.date.today().strftime("%Y-%m-%d")
    ref_id = expense_utils.generate_id()
    expense = {
        "id": ref_id,
        "description": description,
        "category": category,
        "amount": round(amount, 2),
        "date": date
    }
    expenses.append(expense)
    print("Expense added successfully!")
    print("Reference ID:", ref_id)

    choice = input("Add another expense? (yes/no): ")
    if choice.lower() != "yes":
        break
total = expense_utils.calculate_total(expenses)

print("\nTotal Spending:", total)

print("\nCategory Wise Expenses:")
categories = expense_utils.category_total(expenses)
for category, amount in categories.items():
    print(category, ":", amount)

current_month = dt.date.today().strftime("%Y-%m")
monthly_report(expenses, current_month)
file_path = "expense_report.txt"
if os.path.exists(file_path):
    print("Report file already exists.")
else:
    print("No saved report file found.")

print("\nThank you for using Expense Tracker!")