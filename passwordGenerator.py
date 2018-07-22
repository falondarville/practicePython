# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.
import random, string

num_one = str(random.randint(1, 1000))
num_two = str(random.randint(1, 1000))
num_three = str(random.randint(1, 1000))
letter_one = random.choice(string.ascii_letters)
letter_two = random.choice(string.ascii_letters)
letter_three = random.choice(string.ascii_letters)
punctuation = random.choice(string.punctuation)

def generate_password():
	return num_one + letter_one + num_two + letter_two + num_three + letter_three + punctuation

print(generate_password())
