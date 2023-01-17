quiz = {
    "question 1":{
        "question" : "What is the capital of England?",
        "answer" : "London"
    },
    "question 2":{
        "question" : "What is the Capital of France?",
        "answer" : "Paris"
    },
     "question 3":{
        "question" : "What is the only day of the week beginning with 'w'? ",
        "answer" : "Wednesday"
    },
     "question 4":{
        "question" : "What is the 4th letter of the Alphabet?",
        "answer" : "D"
    },
     "question 5":{
        "question" : "What is the sun made of?",
        "answer" : "Gas"
    }
}

score = 0

for key, value in quiz.items():
    print(value["question"])
    answer = input("Answer? :")
    print("")

    if answer.lower() == value["answer"].lower():
        print("Well Done!")
        score = score +1
        print("your score is now "+str(score))
        print("")
    else:
        print("Thats incorrect")
        print("your final score is "+str(score)+"/10 "+str(int(score/5*100))+"%")
        quit(0)

print("congratulations You scored max points!")
print(str(int(score/5*100))+"%")
