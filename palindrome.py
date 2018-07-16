# Ask the user for a string and print out whether this string is a palindrome or not. Takeaway of this exercise is that strings can be treated as lists.
print("Please enter a word.")

word = input()

if word == word[::-1]:
	print("This is a palindrome.")
else:
	print("This is not a palindrome.")
