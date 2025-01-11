import random
import csv

def makequiz():
    global quiz
    global quiznumber
    quiz = []
    quiznumber = random.randint(1,9999)
    for i in range (5):    
        roperator = random.randint(1,4)
        if roperator == 1:
            randint1 = random.randint(1,500)
            randint2 = random.randint(1,500)
            answer = randint1 + randint2
            quiz.append([randint1,"+",randint2,answer])
        if roperator == 2:
            randint1 = random.randint(1,1000)
            randint2 = random.randint(1,randint1)
            answer = randint1 - randint2
            quiz.append([randint1,"-",randint2,answer])
        if roperator == 3:
            randint1 = random.randint(1,32)
            randint2 = random.randint(1,32)
            answer = randint1*randint2
            quiz.append([randint1,"*",randint2,answer])
        if roperator == 4:
            randint2 = random.randint(1,99)
            answer = 1000//randint2
            answer = random.randint(1,answer)
            randint1 = randint2*answer
            quiz.append([randint1,"/",randint2,answer])
def runquiz():
    global score
    global name
    name = input("\nYou are currently taking Quiz "+str(quiznumber)+"\nPlease enter a name to help store this quiz attempt: ")
    score = 0
    for i in range (5):
        while True:
            try:
                print ("\n"+str(quiz[i][0]),quiz[i][1],quiz[i][2])
                inputquiz = int(input("please answer the most recent above question: "))
                if inputquiz == quiz[i][3]:
                    score = score+1
                    print("Correct! The correct answer was",quiz[i][3])
                else:
                    print("Incorrect! The correct answer was",quiz[i][3])
                break
            except:
                print("\nplease only enter a number")
def storequiz():
    file = open("Scores.csv","a")
    file.write(name+", "+str(score)+", 5, "+str(score*20)+"\n")
    file.close()

quizattempted = 2
quiz = []
makequiz()
file = open("Scores.csv","a")
file.write("\nNames, Score, Out of, Percent\nQuiz "+str(quiznumber)+"\n\n")
file.close()

while True:
    try:
        input1 = input("""\n\n1) Take the Quiz
2) View Results
3) Create New Quiz
4) Exit

Select Your Choice (enter a number from 1-4): """)
        if input1 == "1":
            runquiz()
            storequiz()
            quizattempted = 1
        elif input1 == "2":
            if quizattempted != 2:
                file = open("Scores.csv","r")
                scorelist = list(csv.reader(file))
                print("['Names','Score','Out Of','Percent']")
                for i in range(len(scorelist)):
                    if " Out of" not in scorelist[i] and len(scorelist[i]) > 0:
                        print(scorelist[i])
                file.close()
            else:
                print("you must first attempt a quiz to see your results")
        elif input1 == "3":
            if quizattempted == 1:
                makequiz()
                file = open("Scores.csv","a")
                file.write("\nQuiz"+str(quiznumber)+"\n\n")
                file.close()
                quizattempted = 3
            else:
                print("You must first attempt a quiz before creating a new one")
        elif input1 == "4":
            break
        else:
            print("please only enter a number from 1-4")
    except:
        print("error")

print("\nThank you for taking my quiz!")