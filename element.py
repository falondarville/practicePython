# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def check_items(l, i):
	if i in l:
		return True
	else:
		return False

# returns True
print(check_items(items, 3))

# returns Falso
print(check_items(items, 20))

# return False because it is also type checking
print(check_items(items, "3"))