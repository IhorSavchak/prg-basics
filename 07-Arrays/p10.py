categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]
result = 0
counter = 0
for i in expenses:
    counter += 1
    result = max(expenses[counter])

print(categories[result])