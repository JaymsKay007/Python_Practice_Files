''' 
#Instructions#
Congratulations, you've got a job T Python Pizza. Your first job is to build an automatic pizza order
program.
Based on a user's order, work out their final bill.
Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25

Pepperoni for small pizza: +$2
Pepperoni for medium or large pizza: +$3

Extra cheese for any size pizza: +$1

EXAMPLE: INPUT
size = "L"
add_pepperoni = "Y"
extra_cheese = "N"

EXAMPLE: OUTPUT
Your final bill is: $28
'''
print("Welcome to Python Pizza delivery")
size = input("What size pizza do you want? S, M or L. \n")
add_pepperoni = input("Do you want pepperoni? Y or N. \n")
extra_cheese = input("Do you want Extra Cheese? Y or N. \n")

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
else:
    bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}")
