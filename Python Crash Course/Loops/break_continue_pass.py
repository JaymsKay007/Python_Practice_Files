for num in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    if num == 4:
        break
    print(num)
print("This is the code after the for loop.")
#
# BREAK
for num in range(1, 3):
    for letter in "Kingdom":
        if letter == "d":
            break
        print(letter)
    print("___")

# CONTINUE
for num in range(1, 2):
    for letter in "Jaymes":
        if letter == "e":
            print("letter equal 'e' ")
            continue
        print(letter)
    print("___")
