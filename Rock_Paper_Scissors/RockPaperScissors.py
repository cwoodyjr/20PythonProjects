import random

exit_game = False

while exit_game == False:
    user_score = 0
    computer_score = 0
    for x in range(1, 6):
        options = ["Rock", "Paper", "Scissors"]
        print("Attempt number: ", x)
        valid_input = False
        while not valid_input:
            user_input = input("Choose Rock, Paper, Scissors or Exit: ")
            if user_input.lower() in ["rock", "paper", "scissors"]:
                valid_input = True
            elif user_input.lower() == "exit":
                print("Exiting Programme")
                exit_game = True
                break
            else:
                print("Invalid input, please try again")
        if exit_game:
            break
        print("You Chose: ", user_input)
        computer_input = random.choice(options)
        print("Computer Chose: ", computer_input)

        if computer_input.lower() == user_input.lower():
            print("Thats a Tie!!")
        elif computer_input.lower() == "Rock".lower():
            if user_input.lower() == "Paper":
                print("YOU WIN!")
                user_score = user_score+1
            else:
                print("Comouter Wins!")
                computer_score = computer_score+1
        elif computer_input.lower() == "Paper".lower():
            if user_input.lower() == "Scissors".lower():
                print("YOU WIN!!")
                user_score = user_score+1
            else:
                print("computer Wins!")
                computer_score = computer_score+1
        elif computer_input.lower() == "Scissors".lower():
            if user_input.lower() == "Rock".lower():
                print("YOU WIN!!")
                user_score = user_score+1
            else:
                print("computer Wins!")
                computer_score = computer_score+1
        if x == 5:
            print("Thats the end of the game")
            print("You Scored ", user_score)
            print("Computer Scored", computer_score)
            exit_game = True

    if user_score > computer_score:
        print("YOU BEAT THE COMPUTER")
    elif computer_score > user_score:
        print("YOU LOST THE GAME")
    else:
        print("THE GAME ENDED AS A TIE")
