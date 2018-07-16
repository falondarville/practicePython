# Write a program that prints out all the elements of the list that are less than 5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = []

for element in a:
	if element < 5:
		b.append(element)

print(b)

# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
print("Please choose a number.")

chosen = int(input())

d = []

for element in a:
	if element < chosen:
		d.append(element)

print(d)