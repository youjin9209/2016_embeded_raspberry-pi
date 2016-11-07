def check(year):
	return year%400 == 0 or year%4 == 0 and year%100 != 0

while(1):
	year = raw_input("year: ")
	if(year=="esc"):
		print ("Program is terminated...!!!")
		break
	elif(year==""):
		print ("null")
	elif(0 <= int(year)):
		if(check(int(year)) == 1):
			print (int(year)," yoon nyun ok")
		elif(check(int(year)) == 0):
			print (int(year), "not yoon nyun")
