# create a function that adds two arguments, regardless of whether or not they are passed through in parentheses
def sum(*args):
	total = 0
	for i in args:
		total += i
	return total

print(sum((2), (3)))

print(sum(2, 3))