# In the previous exercise we created a dictionary of famous scientists’ birthdays. In this exercise, modify your program from Part 1 to load the birthday dictionary from a JSON file on disk, rather than having the dictionary defined in the program.

import json

with open("info.json", "r") as f:
    info = json.load(f)

print('Welcome to the birthday dictionary. We know the birthdays of:')

for each in info["birthdays"]:
	print(each["name"])

print('Whose birthday do you want to know?')

query = str(input())

print(f'You want to know the birthday of {query}.')

for i in info["birthdays"]:
	if i["name"] == query:
		birthday = i["birthday"]

print(f"{query}'s birthday is on {birthday}")