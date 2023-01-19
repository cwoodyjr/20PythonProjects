import random

exit = False

while exit == False:
    options = ["Rock", "Paper", "Scissors"]
    user_input = input("Choose Rock, Paper, Scissors or Exit: ")
    print("You Chose: ", user_input)
    computer_input = random.choice(options)
    print("Computer Chose: ", computer_input)

    if user_input.lower() == "Exit".lower():
        print("Exiting Programme")
        exit = True
    if computer_input.lower() == user_input.lower():
        print("Thats a Tie!!")
