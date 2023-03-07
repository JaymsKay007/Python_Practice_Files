# SET DIFFERENCE.. this shows the different data in each set{}
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

diff = a.difference(b)
diff1 = a - b
print(diff)
print(diff1)

diff2 = b.difference(a)
diff3 = b - a
print(diff2)
print(diff3)

# SYMMETRIC DIFFERENCE... This show the differences in both set{} and produce the result in 1 set.
sym = a ^ b
sym2 = a.symmetric_difference(b)
print(sym)
print(sym2)
