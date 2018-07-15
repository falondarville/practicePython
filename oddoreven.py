# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
print("Please choose a number.")

num = int(input())

if num % 2 == 0:
	if num % 4 == 0:
		print("This number is a multiple of four.")
	print("This is an even number.")
else:
	print("This is an odd number.")


# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

print("Please choose one number.")

number = int(input())

print("Please choose a second number.")

check = int(input())

if check % number == 0:
	print("The second number divides evenly into the first.")
else:
	print("The second number does not divide evenly into the first.")
