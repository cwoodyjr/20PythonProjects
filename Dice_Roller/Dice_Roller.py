import random
from DiceDict import dice_drawing


def roll_dice():
    roll = input("Roll the dice? (Yes/No) : ")
    while roll.lower() == "Yes". lower() or roll.lower() == "Y". lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print("dice rolled: {} and {}". format(dice1, dice2))
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))
        if dice2 == dice1:
            print("YOU LUCKY PERSON!!")
            print("")
        roll = input("Roll again? (Yes/no): ")
    print("exiting...")
    quit()
    
def roll_doubles():
    roll = input("Roll the dice? (Yes/No) : ")
    while roll.lower() == "Yes". lower() or roll.lower() == "Y". lower():
        dice1 = random.randint(1, 6)  
        dice2 = dice1
        #in ths method we can create 2 instances of dice and make thge 2nd egual to the 1st.
        #or we can use a while loop to generate a random int on the 2nd dice until it equals the 1st
        # e.g:
        # while dice2 != dice1:
        #     dice2 = random.randint(1,6)
            
        print("dice rolled: {} and {}". format(dice1, dice2))
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))
        roll = input("Roll again? (Yes/no): ")
    print("exiting...")
    quit()


user_answer = input("should we roll doubles only? ")
while user_answer.lower() == "Yes". lower() or user_answer.lower() == "Y". lower():
    roll_doubles()
roll_dice()
