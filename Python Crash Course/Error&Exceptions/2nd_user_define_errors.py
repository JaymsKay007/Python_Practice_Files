def play_again():
	replay = input("Do you want to play again?: ")
	if replay.lower() != ["yes", "no"]:
		raise ValueError("Enter Yes or No only.")


play_again()

class