def enter_a_number():
	while True:
		try:
			num = int(input("Enter a number: "))
		except:
			print("That's not a number. Try again.")
			continue
		else:
			# print(num)
			print("Good choice.")
			break
	return num


enter_a_number()
