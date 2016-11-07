score = int(input("total score:"))

if score >= 90:
	print("su")
else:
	if 80 <= scroe < 90:
		print("wu")
	else:
		if 70 <= score < 80:
			print("mi")
		else:
			if 60 <= score < 70:
				print("yang")
			else:
				print("ga")
