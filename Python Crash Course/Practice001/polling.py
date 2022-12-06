"""
    Polling: Use the code in favorite_languages.py (page 97).
• Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
• Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll.
"""
favourite_language = {
    "james": "python",
    "bayoh": "javascript",
    "rashida": "ruby",
    "mohamed": "java",
    "joel": "python",
}
language_poll = ["james", "amie", "johnson", "mohamed", "jack", "rashida"]

for _ in language_poll:
    if _ in favourite_language:
        print(f"{_.title()}, thank you for taking the poll.")
    else:
        print(f"{_.title()}, you're invited to take the favorite language poll.")
