def greet_user():
    user = input("What's your name? ")
    prompt = f"Hello {user.title()}, how was your day?."
    greet = input(prompt)
    print(f"I'm glad you're doing {greet}.")


greet_user()
