import math
import random


def divider(x, y):
	return x / y


try:
	result = divider(24, 2)
	# result = divider(24, "2")
	# result = divider(24, 0)
	# result = divider(24, a)
	result = math.floor(result)
except ZeroDivisionError:
	print("You can't divide by a zero.")

except TypeError:
	print("You mistype a string for a number.")
except NameError:
	print("You mistype a letter for a number.")
except:
	print("Are you sure you're inputting 2 numbers? ")

else:
	print("Everything runs smoothly.")
	print(result)
finally:  # This runs no matter what the condition is.
	print("I always run.")
