# Write a program that takes a list of numbers and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
a = [5, 10, 15, 20, 25]

# note that passing num[0] and num[-1] into list() is not going to work because list() expects one argument and got two
def first_and_last(nums):
 	return [nums[0], nums[-1]]

print(first_and_last(a))