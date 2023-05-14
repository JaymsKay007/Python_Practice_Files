# for num in range(1, 21):
# print(f"I'm number {num}")

# Print from one to 1 million
# for num in range(1, 1000001):
#     print(f"I'm number {num}")

# odd numbers
# for odd in range(1, 20, 2):
#     print(f"The odd number is {odd}")

# Multiples of 3
# for num in range(0, 31, 3):
#     print(num)

# Cubic
# cubic = []
# for num in range(1, 10):
#     cubic.append(num**3)
# print(cubic[:6])  # This slice the 1st 6 numbers in the list.
# print(cubic)

# Slice
players = ["james", "rashida", "Mary", "sal", "tina", "joe", "jane", "michael", "peter", "binta"]

print("Here are the last 5 players in my team:")
for player in players[-5:]:
    print(player.title())

print("\nHere are the first 5 players transferred to my team:")
new_players = [player.title() for player in players[:5]]
print(new_players)
