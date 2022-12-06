"""
Creating a Dictionary.
"""


def add_word():
    # Set a flag to indicate that polling is active.
    words_list = {}
    word_active = True
    while word_active:
        print("Input a word and then define it and it'll be store in the dictionary. ")
        word = input("Input a Word: ")
        word_def = input("What's the meaning of the 'WORD' you input. ")

        # Store the response in the dictionary
        words_list[word] = word_def

        # Find out if anyone else is going to take the poll.
        repeat = input("Would you like to input another word? ('yes' / 'no'). ")
        if repeat == "no":
            word_active = False

            # Polling is complete. Show the results.
            print("\n--- Final Results ---")
        for word, word_def in words_list.items():
            print(f"{word.title()}:\t  {word_def.title()}.")
        print("Your word has been added to the Dictionary, thanks for participating. ")


add_word()
