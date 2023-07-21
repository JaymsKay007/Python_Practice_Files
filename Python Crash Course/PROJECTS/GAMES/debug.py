def get_user_selection():
	choices = ("Rock", "Paper", "Scissors")
	user_input = " "
	while user_input not in choices:
		user_input = input("Enter a choice (rock, paper, scissors): ").capitalize()
		continue
		return user_input


get_user_selection()
