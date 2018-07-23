# Create a program that will play the “cows and bulls” game with the user. The game works like this:

# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout the game and tell the user at the end.
import random

# generate a 4-digit number
num = random.randint(1000, 10000)

# need to separate num into a list of four numbers, so I can check their index and value
num = [int(d) for d in str(num)]

print(num)

print("Please guess a four-digit number.")

user_input = input()
user_input = [int(n) for n in str(user_input)]
print(user_input)

# check that the user's input meets the length requirement
while len(user_input) != 4:
	print("Please choose a four digit number.")
	user_input = input()
	user_input = [int(n) for n in str(user_input)]

# correct in right place = cow
# correct in wrong place = bull
