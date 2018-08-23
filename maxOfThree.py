# Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!
def get_max(num1, num2, num3):
	if num1 > num2 and num1 > num3:
		return num1
	elif num2 > num1 and num2 > num3:
		return num2
	else:
		return num3

print(get_max(1, 2, 3))
