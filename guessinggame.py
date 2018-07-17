# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
import random

random_number = random.randint(1, 10)

user_guesses = 0

print("Please choose a number between 1 and 9.")
user_input = input()

while random_number != int(user_input):
	if random_number > int(user_input):
		print("You guessed too low.")
		user_guesses += 1
		user_input = input()
	elif random_number < int(user_input):
		print("You guessed too high.")
		user_guesses += 1
		user_input = input()
user_guesses += 1
print("That's the same number the computer chose.")
print(f"You guessed a total of {user_guesses} times.")
	