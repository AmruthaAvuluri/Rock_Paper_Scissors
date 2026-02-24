import random

moves = ["rock", "paper", "scissors"]

# Computer chooses first
computer_move = random.choice(moves)
print("Computer has chosen its move!")

# Now user enters move
user_move = input("Now enter rock, paper, or scissors: ").lower()

print("Computer chose:", computer_move)

# Decide winner
if user_move == computer_move:
    print("It's a tie!")
elif user_move == "rock" and computer_move == "scissors":
    print("You win!")
elif user_move == "paper" and computer_move == "rock":
    print("You win!")
elif user_move == "scissors" and computer_move == "paper":
    print("You win!")
else:
    print("Computer wins!")