# This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100. The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.

# At the end of this exchange, your program should print out how many guesses it took to get your number.
from random import randint 

print("Think of a number between 0 and 100 (including 0 and 100), then enter 'go' to let the computer know you're ready to play.")

user_input = input()

still_playing = True
num_guesses = 0

if user_input == "go":
	while still_playing:
		all_guesses = []
		high_num = max(all_guesses)
		low_num = min(all_guesses)
		computer_guess = randint(0, 101)
		print(f"Is {computer_guess} your number?")
		print("Please enter one of the following: 'too high', 'too low', 'you got it'")
		response = input()
		if response == "too high":
			if high_num.length > 0 and low_num.length > 0: 
				computer_guess = randint(low_num, high_num)
			else: 
				computer_guess = randint(0, computer_guess)
			all_guesses.append(computer_guess)
			print(f"Is {computer_guess} your number?")
			print("Please enter one of the following: 'too high', 'too low', 'you got it!'")
			num_guesses += num_guesses
		if response == "too low":
			if high_num.length > 0 and low_num.length > 0: 
				computer_guess = randint(low_num, high_num)
			else: 
				computer_guess = randint(computer_guess, 101)
			all_guesses.append(all_guesses)
			print(f"Is {computer_guess} your number?")
			print("Please enter one of the following: 'too high', 'too low', 'you got it!'")
			num_guesses += num_guesses
		if response == "you got it":
			num_guesses += num_guesses
			print("Yay! I guessed the right number! It took me {num_guesses} times")
			still_playing = False

