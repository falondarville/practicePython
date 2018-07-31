# ask the user what size of board they want and print it!
print("Tell me how many boxes across you would like on your game board.")

user_input = int(input())

def generate_board(i):
	dashes = " --- " * i
	pipes = "|    " * (i +1)

	for x in range(0, i):
		print(dashes)
		print(pipes)
	print(dashes)

generate_board(user_input)