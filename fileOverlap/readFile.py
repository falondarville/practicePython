# Find the numbers that overlap between the two txt files in this folder. 

# read the first txt file
with open("one.txt", "r") as open_file:
	set_one = open_file.read()

set_one = set_one.split("\n")
# print(set_one)

# read the second txt file
with open("two.txt", "r") as open_file:
	set_two = open_file.read()

set_two = set_two.split("\n")
# print(set_two)

overlaping_numbers = [i for i in set_one if i in set_two]
print(overlaping_numbers)
