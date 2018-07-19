# Write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Use list comprehension to solve this. 

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# use the variable as the iterator for each item in the list B if the item appears in list A.
result = [i for i in b if i in a]

print(result)

# the following returns a dictionary
# result = set(a).intersection(set(b))
# print(result)