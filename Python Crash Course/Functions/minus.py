def calculator():
	def subtract():
		num1 = int(input("Enter the 1st number: "))
		num2 = int(input("Enter the 2nd number: "))
		num3 = num1 - num2
		print(num3)

	def add():
		num1 = int(input("Enter the 1st number: "))
		num2 = int(input("Enter the 2nd number: "))
		num3 = num1 + num2
		print(num3)

	def multiply():
		num1 = int(input("Enter the 1st number: "))
		num2 = int(input("Enter the 2nd number: "))
		num3 = num1 * num2
		print(num3)

	subtract()
	add()
	multiply()


calculator()
