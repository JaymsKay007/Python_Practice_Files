a = 1
b = 1
while a <= 5:
    print(f"This is {a} times table.")
    while b <= 12:
        c = a * b
        print(f"{a} * {b} = {c}")
        b += 1
    a += 1
    b = 1
    print("---")
