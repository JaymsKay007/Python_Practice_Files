import wikipedia

question = input("What do you want to search about?: ")
answer = wikipedia.summary(question)
print(answer)
