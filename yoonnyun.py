year = int(input("year: "))
month = int(input("month: "))
day = int(input("day:"))

days = 0

for i in range (1, year):
	if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
		days += 366
	else:
		days += 365

for i in range (1, month):
	if (i == 1):
		days += 31
	elif i == 2:
		if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
			days += 29
		else: days += 28
	elif i == 3:
		days += 31
	elif i == 4:
		days += 30
	elif i == 5:
		days += 31
	elif i == 6:
		days += 30
	elif i == 7:
		days += 31
	elif i == 8:
		days += 31
	elif i == 9:
		days += 30
	elif i == 10:
		days += 31
	elif i == 11:
		days += 30
	elif i == 12:
		days += 31


days += day

weekday = days%7

if weekday == 1:
	print('monday')
elif weekday == 2:
	print('Tuesday') 
elif weekday == 3:
	print('Wednesday')
elif weekday == 4:
	print('Thursday')
elif weekday == 5:
	print('Friday')
elif weekday == 6:
	print('Saturday')
elif weekday == 0:
	print('Sunday')

