current_number = int(input("Input number from 1 to 10: "))

if current_number > 10:
    print("You input wrong number, please input from 1 to 10.")
else:
    while current_number <= 10:
        print(current_number)
        current_number += 1
