b = 1
for a in range(1, 6):
    print(f"This is {a} times table.")
    while b <= 12:
        c = a * b
        print(f"{a} * {b} = {c}")
        b += 1
    b = 1
    print("---")
