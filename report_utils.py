from tabulate import tabulate

def monthly_report(expenses, month):
    data = []
    for e in expenses:
        if e["date"][:7] == month:

            data.append([
                e["id"],
                e["date"],
                e["description"],
                e["category"],
                e["amount"]
            ])
    print("\nMONTHLY EXPENSE REPORT")
    print(tabulate(
        data,
        headers=["ID", "Date", "Description",
                 "Category", "Amount"],
        tablefmt="grid"
    ))
