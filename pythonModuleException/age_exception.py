class AgeException(Exception):
	def __init__(self, msg):
		self._message = msg

	def input_age():
		age = int(input("input age:"))
		if age < 0:
			raise AgeException("age should be over Zero")
		elif age > 150:
			raise AgeException("how could you live over 150?")
		else:
			return age

	if __name__ == "__main__":
		try:
			age = input_age()
		except AgeException as e:
			print(e.args[0])
		else:
			print("your age %d " %age)
