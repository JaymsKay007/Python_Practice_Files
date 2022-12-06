"""
Movie Tickets: A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.
"""
prompt = "Welcome to the Best Cinema."
prompt += "How old are you? "

while True:
    age = int(input(prompt))
    if age < 3:
        print(f"The ticket is free for people at {age}yrs old.")

    elif age <= 12:
        print(f"The ticket price is $10 for people at {age}yrs old.")

    elif age > 12:
        print(f"The ticket price is $15 for people at {age}yrs old.")

    else:
        break
