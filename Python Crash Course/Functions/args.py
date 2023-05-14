# ARGS = This takes any amount of variables as the function parameters

# """This function (*args) takes players names and welcome them to the team"""
def game_players(*names):
    for name in names:
        print(f"Hello {name.title()}, welcome to the team.")


game_players("james", "mohamed", "joel")


# """This function adds numbers and give the total sum"""
def add_machine(*numbers):
    return sum(numbers)


final_sum = add_machine(125, 10, 57, 54)
print(final_sum)
