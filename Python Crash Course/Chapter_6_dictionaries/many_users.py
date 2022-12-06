# Dictionary in dictionary...
users = {
    "jameskay": {"first": "james", "last": "kay", "location": "england", },
    "rashkay": {"first": "rashida", "last": "kay", "location": "america", },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    fullname = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFullname: {fullname.title()}")
    print(f"\tLocation: {location.title()}")
