###
# Calculates the number of days in a month
#
month = int(input('Enter month number (1..12)'))
checker = True
if month % 2 == 0:
    checker = True
else:
    checker = False

if checker == False and month != 2 :
    days = 31 ## months with 31 days
elif checker == True and month != 2:
    days = 30
elif month==2:
    days = 28

print(f'Month {month} has {days} days')