import random
def generate_id():
    return "EXP-" + str(random.randint(1000, 9999))

def validate_amount(amount):
    if amount > 0:
        return True
    else:
        return False

def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total = total + expense["amount"]
    return round(total, 2)

def category_total(expenses):
    result = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in result:
            result[category] += amount
        else:
            result[category] = amount
    return result