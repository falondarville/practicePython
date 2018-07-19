# Ask the user for a number and determine whether the number is prime or not. A prime number is a number that has no divisor. 

print("Please enter a number.")

user_input = int(input())

if user_input > 0:
	# Make a range containing numbers 2 through user_input - 2, since prime numbers are divisible by one and themselves only. We don't want to include these, or the number will not be recognized as prime. For each item in this range, iterate through and divide the user number by it. If the number is divisible by any of the numbers in this range, it is not prime. 
	check_range = range(2, user_input-1)

	list_non_prime = [i for i in check_range if user_input % i == 0]

	if len(list_non_prime) > 0:
		print("This number is not prime.")
	else:
		print("This number is prime.")