"""
Moving Items from One List to Another...
Consider a list of newly registered but unverified users of a website. After
we verify these users, how can we move them to a separate list of confirmed
users? One way would be to use a while loop to pull users from the list of
unconfirmed users as we verify them and then add them to a separate list of
confirmed users.
"""
# Start with users that need to be verified, and an empty list to hold confirmed users.
unconfirmed_users = ["James", "Tina", "Rashida", "Mohamed"]
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying users: {current_user.title()}")
    # Display all confirmed users.
    confirmed_users.append(current_user)
    print("\nThe following users have been confirmed:")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())
