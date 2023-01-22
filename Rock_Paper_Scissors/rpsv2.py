import random

# Initialize variables
user_score = 0
computer_score = 0
round_number = 1
exit = False

# Game loop
while not exit:
    # Print round number
    print(f'Round {round_number}:')

    # Get user input
    user_input = input("Choose Rock, Paper, or Scissors or type 'exit' to quit: ").lower()

    # Handle exit
    if user_input == "exit":
        print("Exiting game...")
        exit = True
        continue

    # Handle invalid input
    while user_input not in ["rock", "paper", "scissors"]:
        print("Invalid input. Please try again.")
        user_input = input("Choose Rock, Paper, or Scissors or type 'exit' to quit: ").lower()

    # Get computer input
    computer_input = random.choice(["rock", "paper", "scissors"])

    # Compare inputs
    if user_input == computer_input:
        print("It's a tie!")
    elif (user_input == "rock" and computer_input == "scissors") or (user_input == "paper" and computer_input == "rock") or (user_input == "scissors" and computer_input == "paper"):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    # Check for end of game
    if round_number == 5:
        print("Game over!")
        print(f'Your score: {user_score}')
        print(f'Computer score: {computer_score}')
        exit = True
    else:
        round_number += 1
