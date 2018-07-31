# ask the user what size of board they want and print it!
print("Tell me how many boxes across you would like on your game board.")

user_input = int(input())

def generate_board(i):
	print(" --- " * i)
	print("   |   " * i)
	print(" --- " * i)

generate_board(user_input)