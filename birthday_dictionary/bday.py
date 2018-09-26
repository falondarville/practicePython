# For this exercise, we will keep track of when our friend’s birthdays are, and be able to find that information based on their name. Create a dictionary (in your file) of names and birthdays. When you run your program it should ask the user to enter a name, and return the birthday of that person back to them. 

birthday_list = {'Albert Einstein': '03/14/1879', "Ada Lovelace": '12/10/1815', "Benjamin Franklin": '01/17/1706'}

print('Welcome to the birthday dictionary. We know the birthdays of:')

for name in birthday_list:
	print(name)

print('Whose birthday do you want to know?')

query = str(input())

print(f'You want to know the birthday of {query}.')

birthday = birthday_list[query]

print(f"{query}'s birthday is on {birthday}")