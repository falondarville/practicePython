# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …
def check_fibonacci():
	print("How many Fibonnaci sequence numbers would you like to generate?")
	user_input = int(input())
	# generate the sequence on the fly or hard code it?
	# take the user_input, which will be a single number, and use this to generate the number of numbers that will return. 
	i = 1
	if user_input == 0:
		sequence = []
	elif user_input == 1:
		sequence = [1]
	elif user_input == 2:
		sequence = [1, 1]
	elif user_input > 2:
		sequence = [1, 1]
		while i < (user_input -1):
			sequence.append(sequence[i] + sequence[i-1])
			i += 1

	return sequence

print(check_fibonacci())