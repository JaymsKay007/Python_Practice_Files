import math

"""
INSTRUCTIONS
You're painting a wall and the instruction on the paint_can says 1 Can of paint can cover 5 square meters of wall.
Given a random height and width of wall, calculate how many cans of paint will you need to buy. 

FORMULA
number of cans = (wall height x wall width)/ coverage per can

e.g. Height = 2, Width = 4, Coverage = 5
number of cans (2 x 4) / 5
1.6

But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.
"""
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5


def paint_calc(height, width, cover):
    area = height * width
    numb_of_can = math.ceil(area / cover)  # math.ceil round up the decimal to a whole number.
    print(f"You'll need {numb_of_can} of paint.")


paint_calc(height=test_h, width=test_w, cover=coverage)
