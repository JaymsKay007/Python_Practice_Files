def fizz_buzz():
    start = int(input("Input your first number to check: "))
    end = int(input("Input your last number to check: "))

    for num in range(start, end):
        if num % 3 == 0 and num % 5 == 0:
            print("Fizz Buzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)


fizz_buzz()
