classgrades = {}
import statistics
def inputgrades():  #runs the system of inputting a new assignment and grades
    global classgrades
    while True:
        try:
            assignmentname = input("\nEnter the name of your assignment: ") 
            if assignmentname not in classgrades: #if an assignment name is reused, when looking at the assignment grades, one will become inaccessible
                classgrades[assignmentname] = {}
                break
            else:
                print("That assignment name has already been inputted. Please enter another")
        except:
            print("not a valid input")
    while True:
        try:
            studentnumber = int(input("\nhow many student's grades do you wish to enter?: "))
            if studentnumber >0:
                break
            else:
                print("you must input at least 1 student's grade")
        except:
            print("please only enter a number")
    while True:
        try:
            assignmentvalue = int(input("\nwhat is the total assignment value (what is it out of (/x) )?: "))
            if studentnumber > 0:
                break
            else:
                print("the assignment must be out of a number greater than zero")
        except:
            print("please only enter a number")
    for i in range(studentnumber):
        while True:
            try:
                student = input("\nenter a student's name: ")
                if student not in classgrades[assignmentname]:
                    mark = int(input("enter the mark they recieved (x/): "))
                    if mark <= assignmentvalue and mark >= 0:
                        classgrades[assignmentname][student] = mark #inputs the students name as the key in the assignment subdictionary, and their mark are the value
                        break
                    else:
                        print("the mark a student recieves cannot exceed %100 or be less than 0")
                else:
                    print("That name is already in use for this current assignment. Please select another one or change any letter in it")
            except:
                print("please only enter a valid variable")
    classgrades[assignmentname]["averages"] = [int(statistics.mean(classgrades[assignmentname].values())), #calculates and stores the mean, median, and mode into the designated assignments dictionary as a list
    int(statistics.mode(classgrades[assignmentname].values())),int(statistics.median(classgrades[assignmentname].values()))]
    classgrades[assignmentname]["outof"]= assignmentvalue #adds what the assignment was made out of because that was not stored in a student's value
def printaassignment(x): #allows the user to see previous assignments and what marks were recieved
    print("\nThe",x,"assignment:")
    y = list(classgrades[x].keys()) #provides easier access to the students in the dictionary
    w = list(classgrades[x].values()) # provides easier access to the marks in the dictionary
    for i in range(len(classgrades[x])-2): #the last two variables are not student marks so they are not included (they are what the project is out of and its averages)
        print(y[i],"recieved a",w[i],"/",w[-1],"(%",(int(w[i]/w[-1]*100)),")") #prints each students mark
    print("\nThe total class average for this assignment is",w[-2][0],"/",w[-1],"(%",int(w[-2][0]/w[-1]*100),")" #prints the averages
    ,"\nThe class median for this assignment is",w[-2][2],"/",w[-1],"(%",int(w[-2][2]/w[-1]*100),")"
    ,"\nThe class mode for this assignment is",w[-2][1],"/",w[-1],"(%",int(w[-2][1]/w[-1]*100),")")
def menuprint(): #prints the menu
        print("""\n\n-----------Menu-----------
1) Enter an Assignment
2) View Past Marks of An Assignment
3) View Past Marks of A Student
4) Exit          
------------------""")
def menu(): #runs all other functions and the game
    while True:
        try:
            menuprint()
            input1 = int(input("choose your option (enter a number from 1-3): "))
            if input1 > 0 and input1 < 5:
                if input1 == 1:
                    inputgrades()
                elif input1 == 2:
                    if len(classgrades) > 0:
                        while True:
                            print (list(classgrades.keys()))
                            assignmentview = input("Which of the above assignments do you wish to view the marks of?: ")
                            if assignmentview in classgrades:
                                printaassignment(assignmentview)
                                break
                            else:
                                print("\nyou must select the name of an assignment from the above list")
                    else:
                        print("you must first enter an assignment to view the marks of one")
                elif input1 == 3:
                    studenttrue = 5 #this variable checks if the name exists or not, or if there were names inputted to begin with, and prints a message based on this
                    if len(classgrades) > 0:
                            studenttrue = False
                            paststudent = input("please enter the name of a student you have already entered into the system: ")
                            for i in range(len(classgrades)): #this and the next two lines of code check if a student name is in the dictionary storing all marks
                                allassignments = list(classgrades.keys())
                                if paststudent in classgrades[allassignments[i]]:
                                    print("\n",paststudent,"recieved a",classgrades[allassignments[i]][paststudent],"/", #a long print statement which prints all marks a student has recieved
                                        classgrades[allassignments[i]]["outof"],"(%",(int(classgrades[allassignments[i]]
                                [paststudent]/classgrades[allassignments[i]]["outof"]*100)),") on the assignment:",allassignments[i])
                                    studenttrue = True
                    if studenttrue == 5:
                        print("there are currently no entered student marks to show")
                    elif studenttrue == True:
                        print("")
                    elif studenttrue == False:
                        print("There are no students with your inputted name")
                elif input1 == 4:
                    return
            else:
                print("please only enter a number from 1-3")
        except:
            print("please only enter a number from 1-3")


menu()
print("Thank you for viewing my marking system")