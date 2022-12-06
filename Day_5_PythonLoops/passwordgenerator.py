import random
# We're going to crate a password generator that create strong passsword for users.
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
           "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))

# HARD Method
password_list = []

for _char in range(1, nr_letters + 1):
    password_list += random.choice(letters)

for _char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

for _char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

# make the password into a string and return it to the user.
PASSWORD = ""
for char in password_list:
    PASSWORD += char
    random.shuffle(password_list)
print(f"Your password is {PASSWORD}")


# EASY Method
# password = ""

# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)

# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)

# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)

# print(password)
