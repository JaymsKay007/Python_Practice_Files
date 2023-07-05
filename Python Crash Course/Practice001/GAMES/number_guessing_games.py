"""
THE NUMBER GUESSING GAME...
This game will:
1. Get the computer to generate a random number.
2. Allow the user to submit a guess.
3. Produce game logic using conditional statements:
	-If guess is too high, the player should get a message.
	-If guess is too low, the player should get a message.
	-If guess is too correct, the player should get a message.
4. A player should only get 5 guesses. Once the guess run out, the games is over
5. A player should get asked if they want to play again, if Yes, replay the game, if No,
break out of the game.
"""
import random

num = random.randint(1, 100)  # This generates random number from 1 to 100


# GAME LOGIC
def game_logic():
	guess = 0
	tries = 5
	while guess != num and tries != 0:
		guess = input("Guess a number between 1 and 100: ")
		guess = int(guess)

		if guess == num:
			print("Congratulations! You guessed correctly.")

		elif guess != num and tries == 1:
			print("Better luck next time! ")
			print(f"The correct hidden number is {num}.")
			break
		# Out of range guesses.
		elif guess > 100:
			print(f"Wrong number, {guess} is out of range.")
		elif guess < 0:
			print("Wrong number, can't accept negative number.")

		elif guess > num:
			tries -= 1
			print(f"You guessed too high. Try a lower number. You've {tries} chance left.")
		else:
			tries -= 1
			print(f"You guessed too low. Try a higher number. You've {tries} chance left.")


# THIS ASK THE USER IF THEY WANT TO PLAY AGAIN...
def play_again():
	again = ""
	while again.lower() not in ["y", "n"]:
		again = input("Do you want to play again? (Y/N):")
		if again.lower() == "y":
			return True
		elif again.lower() == "n":
			return False


while True:
	# num = random.randint(1, 100)
	# tries = 5
	# guess = None
	print("""Welcome to the number guessing game. You have 5 guesses.""")
	game_logic()

	if not play_again():
		print("See you next time.")
		break
