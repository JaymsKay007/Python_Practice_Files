def request_age():
	age = ""
	while not age.isdigit():
		age = input("What's your age?: ")
		if not age.isdigit():
			print("Please enter digits only")
	return int(age)


request_age()
