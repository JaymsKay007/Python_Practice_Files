"""
		ROCK, PAPER, SCISSORS...
Games Ltd want ot add to their collection of online games. They would like
you to produce a version of the popular Rock, Paper, Scissors game!

The application should:
* Obtain a computer generated selection.
* Allow a user to pick Rock, Paper, Scissors.
* Compare the selections and observe whether it is a draw or win.
		Rock smashes scissors (win)
		Paper covers rock (win)
		Scissors cut paper (win)
* Keep track of the score.

The application can be broken down into the following tasks:
1. Create a function that can obtains the users input.
2. Create a function that generates a randomly selected choice for the computer.
3. Determine the winner for each round and keep track of the score.
4. Create a function that checks to see if a user wants to play the game again.
5. Produce a working game using a while loop.
"""
import random


# GAME LOGIC
# 1. Create a function that can obtains the users input.
def get_user_selection():
	choices = ('Rock', 'Paper', 'Scissors')
	user_input = ' '
	while user_input not in choices:
		user_input = input("Enter a choice (rock, paper, scissors): ").capitalize()
		continue
	return user_input


# 2. Create a function that generates a randomly selected choice for the computer.
def computer_generated_selection():
	choices = ['Rock', 'Paper', 'Scissors']
	computer_selection = random.choice(choices)
	return computer_selection


# 3. Determine a winner for each round and keep a track of the score.
player_score = 0
computer_score = 0


def determine_winner(player_choice, computer_choice):
	global player_score
	global computer_score

	if player_choice == computer_choice:
		print(f"Both player selected {computer_choice}. It's a draw!.")

	elif player_choice == "Rock":
		if computer_choice == "Scissors":
			print("Rock smashes Scissors! You win.")
			player_score += 1
		else:
			print("Paper cover Scissors! You lose!")
			computer_score += 1

	elif player_choice == "Paper":
		if computer_choice == "Rock":
			print("Paper covers Rock! You win.")
			player_score += 1
		else:
			print("Scissor cuts Paper! You lose!")
			computer_score += 1

	elif player_choice == "Scissors":
		if computer_choice == "Paper":
			print("Scissors cuts Paper! You win!")
			player_score += 1
		else:
			print("Rock smashes Scissors! you lose!")
			computer_score += 1


#  4. Create a function that checks to see if a user wants to play the game again.
def play_again():
	replay = input("Would you like to play again? (Y/N): ")
	if replay.lower() == "y":
		return True
	elif replay.lower() == "n":
		return False
	else:
		print("Input only 'Y' or 'N'")


# 5. Produce a working game using a while loop.
# player_score = 0
# computer_score = 0
while True:

	print("Welcome to the Rock, Paper, Scissors Arena!")
	print("The Current score is: ")
	print(f"Player {player_score} | {computer_score} Computer.")

	player_choice = get_user_selection()
	computer_choice = computer_generated_selection()

	print(f"You choose {player_choice}, Computer choose {computer_choice}")
	determine_winner(player_choice, computer_choice)

	print("The Current score is: ")
	print(f"Player {player_score} | {computer_score} Computer.")

	if not play_again():
		print("See you soon!")
		break
