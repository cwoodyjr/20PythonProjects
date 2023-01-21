import random

def play_game():
    options = ["Rock", "Paper", "Scissors"]
    user_score = 0
    computer_score = 0

    for round in range(1, 6):
        print(f"Round {round}")

        user_choice = input("Choose Rock, Paper, Scissors or Exit: ")
        if user_choice.lower() == "exit":
            print("Exiting game")
            return

        if user_choice not in options:
            print("Invalid choice, please try again")
            continue

        computer_choice = random.choice(options)
        print(f"You chose {user_choice}, computer chose {computer_choice}")

        if user_choice == computer_choice:
            print("Tie")
        elif (user_choice == "Rock" and computer_choice == "Scissors") or (user_choice == "Paper" and computer_choice == "Rock") or (user_choice == "Scissors" and computer_choice == "Paper"):
            print("You win!")
            user_score += 1
        else:
            print("Computer wins")
            computer_score += 1

    print("Game over")
    if user_score > computer_score:
        print("You won the game!")
    elif user_score < computer_score:
        print("You lost the game!")
    else:
        print("The game was a tie!")
    print(f"Your score: {user_score}, Computer score: {computer_score}")

play_game()
