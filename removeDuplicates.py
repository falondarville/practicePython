# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
l = [1, 1, 1, 3, 4, 6, 6, 7, 19]

def remove_dups(data):
	return list(set(data))

print(remove_dups(l))