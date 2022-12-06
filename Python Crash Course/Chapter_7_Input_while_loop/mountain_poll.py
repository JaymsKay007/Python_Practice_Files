"""
Filling a Dictionary with User Input
You can prompt for as much input as you need in each pass through a while
loop. Let’s make a polling program in which each pass through the loop
prompts for the participant’s name and response. We’ll store the data we
gather in a dictionary, because we want to connect each response with a
particular user:
"""
# Create an empty dictionary...
responses = {}
# Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
    # Prompt for the person's name and response.
    name = input("What's your name? ")
    response = input("What's your dream car? ")
    # Store the response in the dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? ('yes' / 'no') ")
    if repeat == 'no':
        polling_active = False

    # Polling is complete. Show the results.
    print("\n--- Poll Results ---")
    for name, response in responses.items():
        print(f"{name.title()} dream car is {response.title()}.")
