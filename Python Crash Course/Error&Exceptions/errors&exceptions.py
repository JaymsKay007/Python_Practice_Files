# This code print all the python exceptions
#  print(dir(locals()['__builtins__']))

age = "thirty"

if age != int:
	raise TypeError("Sorry, only integers are allowed.")
