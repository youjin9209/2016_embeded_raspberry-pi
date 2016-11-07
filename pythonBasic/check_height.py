age = int(input("age:"))
height = int(input("height:"))

if age >= 40:
	if height >= 170:
		print("over normal.")
	else:
		print("normal.")
else:
	if height >= 175:
		print("over normal.")
	else:
		print("normal.")
