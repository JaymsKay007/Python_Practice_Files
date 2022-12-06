''' 
Write a program that works out whether if a given number is an odd or even number.
Even number can be divided by 2 with no remainder. e.g. 86 / 2 = 43
43 does not have any decimal p;aces. Therefore the division is clean.
e.g. 59 is odd because 59/2 = 36.875
36.875 is not a whole number, it has decimal places. Therefore there's a remainder of .875, 
so the division is not clean. 

The modulo is written as percentage sign(%) in python. It gives you the remainder after a division. 
e.g 6 / 2 = 3 with no remainder
'''
number = int(input("What number do you want to check? "))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number")
