def fizz_buzz():
    start = int(input("Input your first number to check: "))
    end = int(input("Input your last number to check: "))

    while start <= end:
        if start % 3 == 0 and start % 5 == 0:
            print("Fizz Buzz")
        elif start % 3 == 0:
            print("Fizz")
        elif start % 5 == 0:
            print("Buzz")
        else:
            print(start)
        start += 1


fizz_buzz()
