# write a program that returns a list that contains only the elements that are common between the lists (without duplicates)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Using list comprehension, check if the value appears in list b and assign this to list variable c. This comprehension needs to be inside square brackets or it will break. 
c = [val for val in a if val in b]

print(c)