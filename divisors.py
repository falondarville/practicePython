# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. A divisor is a number that divides evenly into another number.
print("Please choose a number.")

num = int(input())

# Create a range that ends with the number inputted and check the numbers below to see if they will evenly divide into the number provided. 
x = range(1, num)
y = []

for element in x:
	if num % element == 0:
		y.append(element)
print(y)
