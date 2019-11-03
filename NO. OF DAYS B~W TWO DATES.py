from datetime import date

print(" ")
print('"NO. OF DAYS B/W TWO DATES"')

print("              ")
print("Enter Min Date:")
print("              ")

day1 = int(input('"Day": '))
month1 = int(input('"Month": '))
year1 = int(input('"Year": '))

print("              ")
print("Enter Max Date:")
print("              ")

day2 = int(input('"Date": '))
month2 = int(input('"Month": '))
year2 = int(input('"Year": '))


f_date = date(year1, month1, day1)
l_date = date(year2, month2, day2)
delta = l_date - f_date

print("           ")
print("No. Of Days: " + str(delta))