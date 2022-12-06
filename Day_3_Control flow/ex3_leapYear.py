'''
Write a program that works out whether if a given year is a leap year. A normal year has 365 days,
leap year has 366 days, with an extra day in February.

This is how you work out whether if a particular year is a leap year.
"On every year that is evenly divisible by 4
    except every year that is evenly divisible 100
        unless the year is also divisible by 400.

E.g. the year 2000
2000 / 4 = 500 (leap)
2000 / 100 = 20 (not leap)
2000 / 400 = 5 (not leap)S
So the year 2000 is a leap year.
'''
year = int(input("Which year do you want to check?"))
# if year % 4 == 0:
# if year % 100 == 0:
# if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not a leap year")  
#     else:
#         print("Leap year")
# else:
#     print("Not a leap year")

# 2nd Method
if year % 4 == 0:
    if (year % 100 == 0) and (year % 400 == 0) or (year % 100 != 0):
        print("Leap year")
    else:
        print("Not a leap year")
else:
    print("Not a leap year")
