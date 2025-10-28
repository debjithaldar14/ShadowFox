
# 5. DICTIONARY

friends = ["Aditya", "Rohit", "Sneha", "Priya", "Arjun"]
name_length = [(name, len(name)) for name in friends]
print("Friends and their name lengths:", name_length)

your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print("Your total expenses:", your_total)
print("Partner's total expenses:", partner_total)

if your_total > partner_total:
    print("You spent more.")
elif your_total < partner_total:
    print("Your partner spent more.")
else:
    print("Both spent the same amount.")

max_diff = 0
category = ""
for key in your_expenses:
    diff = abs(your_expenses[key] - partner_expenses[key])
    if diff > max_diff:
        max_diff = diff
        category = key

print(f"Category with highest spending difference: {category} (Difference: {max_diff})")
