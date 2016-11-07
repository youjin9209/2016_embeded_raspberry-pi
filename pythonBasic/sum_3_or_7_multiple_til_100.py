total = 0

for item in range(1, 101):
	if (item % 3) == 0 or (item % 7) == 0:
		total = total + item

print("multiple 3 or 7 summation 1 to 100", total)
