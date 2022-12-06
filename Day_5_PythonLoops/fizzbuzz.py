for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number% 3 == 0:
        print("Fizz")
    elif number% 5 == 0:
        print("Buzz")
    else:
        print(number)
        
password_list = []
for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

# print(password_list)
# random.shuffle(password_list)
# print(password_list)

# Make the password into a string
password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")