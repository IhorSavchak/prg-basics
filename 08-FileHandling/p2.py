
file = open("numbers.txt", "r")

total = 0

for line in file:
    total += int(line.strip()) 

file.close()

print(total)
