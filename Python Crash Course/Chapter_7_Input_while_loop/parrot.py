prompt = "\nTell me something and I'll repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

# msg = ""
# while msg != "quit":
#     msg = input(prompt)
#     print(msg)

# 2nd option
active = True
while active:
    msg = input(prompt)
    if msg == 'quit':
        active = False
    else:
        print(msg)
