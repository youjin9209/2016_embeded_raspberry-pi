def check(year):
	return year%400 == 0 or year%4 == 0 and year%100 != 0

month30 = [4,6,9,11]
month31 = [1,3,5,7,8,10,11]

year = int(input("year: "))
month = int(input("month: "))
day = int(input("day: "))

n = 0

for i in range(1, year):
	if check(i) == 1:
		n += 2
	else:
		n += 1

for i in range(1, month):
	if i in month30:
		n += 2
	elif i in month31:
		n += 3
	elif i == 2 and check(year) == 1:
		n += 1

n += day-1
n %= 7

dayofweek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Satday', 'Sunday']
print dayofweek[n]
