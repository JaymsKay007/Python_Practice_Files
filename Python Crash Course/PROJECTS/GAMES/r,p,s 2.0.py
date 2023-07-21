import random


def play_game():
	print("Let's play Rock, Paper, Scissors!")
	print("Choose one: (1) Rock, (2) Paper, (3) Scissors")
	player_choice = int(input("Enter your choice (1-3): "))

	while player_choice < 1 or player_choice > 3:
		print("Invalid choice. Please try again.")
		player_choice = int(input("Enter your choice (1-3): "))

	if player_choice == 1:
		player_move = "Rock"
	elif player_choice == 2:
		player_move = "Paper"
	else:
		player_move = "Scissors"

	computer_choice = random.randint(1, 3)

	if computer_choice == 1:
		computer_move = "Rock"
	elif computer_choice == 2:
		computer_move = "Paper"
	else:
		computer_move = "Scissors"

	print("You chose:", player_move)
	print("Computer chose:", computer_move)

	if player_choice == computer_choice:
		print("It's a tie!")
	elif (player_choice == 1 and computer_choice == 3) or \
			(player_choice == 2 and computer_choice == 1) or \
			(player_choice == 3 and computer_choice == 2):
		print("You win!")
	else:
		print("Computer wins!")


def play_again():
	replay = input("Would you like to play again? (Y/N): ")
	if replay.lower() == "y":
		return True
	elif replay.lower() == "n":
		return False
	else:
		print("Input only 'Y' or 'N'")
		play_again()
		play_game()


while True:
	print("Welcome to the Rock, Paper, Scissors Arena!")
	play_game()

	if not play_again():
		print("See you soon!")
		break
