votes = {}
polling_active = True
while polling_active:
    name = input("What's your name? ")
    party = input("Which party do you belong to? ")
    votes[name] = party

    repeat = input("Would you like to let another person respond? ('yes' / 'no') ")
    if repeat == 'no':
        polling_active = False
    # Polling is complete. Show the results.
    print("\n--- Poll Results ---")
    for name, party in votes.items():
        print(f"{name.title()} belongs to {party.upper()} party.")
