import openai

import os

import pandas as pd

import time

openai.api_key = "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"
messages = [
	{"role": "system", "content": "You’re a kind helpful assistant"}
]
while True:
	content = input("User: ")
	messages.append({"role": "user", "content": content})

	completion = openai.ChatCompletion.create(
		model="gpt-3.5-turbo",
		messages=messages
	)

	chat_response = completion.choices[0].message.content
	print(f'ChatGPT: {chat_response}')
	messages.append({"role": "assistant", "content": chat_response})
