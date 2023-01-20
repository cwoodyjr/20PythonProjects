import random

exit = False

while exit == False:
    for x in range(6):
        options = ["Rock", "Paper", "Scissors"]
        print("Attempt number: ",x)
        user_input = input("Choose Rock, Paper, Scissors or Exit: ")
        print("You Chose: ", user_input)
        computer_input = random.choice(options)
        print("Computer Chose: ", computer_input)

        user_score = 0
        computer_score = 0

        if user_input.lower() == "Exit".lower():
            print("Exiting Programme")
            exit = True
        elif computer_input.lower() == user_input.lower():
            print("Thats a Tie!!")
        elif computer_input.lower() == "Rock".lower():
            if user_input.lower() == "Paper":
                print("YOU WIN!")
                user_score += 1
            else:
                print("Comouter Wins!")
                computer_score += 1
        elif computer_input.lower() == "Paper".lower():
            if user_input.lower() == "Scissors".lower():
                print("YOU WIN!!")
                user_score += 1
            else:
                print("computer Wins!")
                computer_score += 1
        elif computer_input.lower() == "Scissors".lower():
            if user_input.lower() == "Rock".lower():
                print("YOU WIN!!")
                user_score += 1
            else:
                print("computer Wins!")
                computer_score += 1
        if x == 5:
            exit = True

print("Thats the end of the game")
print("You Scored ",user_score)
print("Computer Scored", computer_score)

if user_score > computer_score:
    print("YOU BEAT THE COMPUTER")
elif computer_score > user_score:
    print("YOU LOST THE GAME")
else:
    print("THE GAME ENDED IN A TIE")
