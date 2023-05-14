# NESTED FOR LOOP
for a in ["I play", "I watch", "I enjoy"]:
    for b in ["golf", "tennis", "soccer"]:
        print(a, b)
    print("---")

b = 1
for a in range(1, 6):
    print(f"This is {a} times table.")
    while b <= 12:
        c = a * b
        print(f"{a} * {b} = {c}")
        b += 1
    b = 1
    print("---")
