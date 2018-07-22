# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. 
print("Please enter a sentence with multiple words.")

sentence = input()

def reverse_string(s):
	result = s.split(" ")[::-1]
	print(result)

reverse_string(sentence)
