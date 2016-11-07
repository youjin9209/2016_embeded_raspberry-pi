break_letter = input("break letter: ")

for letter in "python":
	if letter == break_letter:
		break
	print(letter)
else:
	print("all letter print completed")
