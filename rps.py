# Make a two-player Rock-Paper-Scissors game. 
player_one_score = 0
player_two_score = 0

while player_two_score < 2 and player_one_score < 2:
	print("Player one, please choose rock, paper, or scissors.")
	player_one_choice = input()
	print("Player one, please choose rock, paper, or scissors.")
	player_two_choice = input()
	if player_one_choice == player_two_choice:
		print("You tied.")
	elif player_one_choice == "paper" and player_two_choice == "rock":
		print("Player one wins.")
		player_one_score += 1
	elif player_one_choice == "scissors" and player_two_choice == "paper":
		print("Player one wins.")
		player_one_score += 1
	elif player_one_choice == "rock" and player_two_choice == "scissors":
		print("Player one wins.")
		player_one_score += 1
	else:
		print("Player two wins.")
		player_two_score += 1
print(f"Player one: {player_one_score} Player two: {player_two_score}")
