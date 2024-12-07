import random
def othervariables(): #defines certain variables which will change as a result of multiple games, or stay the same.
    global ainames
    global recentgames
    global player1score
    global player2score
    global aiscore
    global streak
    ainames = ["Jimmy","Magnus","Reese","Marie","Ivan","Michael","Stephan","Andrew","Matthew","Luke","Niomi","Megan","Lily","Summer"]
    recentgames = []
    player1score = 0
    player2score= 0
    aiscore=0
    streak = {"ai":0,"player1":0,"player2":0}
def reset():  #defines variables that will be reset each time a new game is started  
    global twoplayer #alows the user to input whether they want to play against the ai or against another human
    global movefirst #allows the input to choose whether they want to go first or second when playing against the ai
    global win #When the function 'wincheck' finds that a player has won, the information will be stored here
    global board #the board which stores X's and O's which is shown to the player
    global computerboard # this variable is a fake copy of the game board. It helps distinguish between which squares have been selected.
    global player1name #stores player1s inputed name
    global player2name #in two player mode, stores player 2's inputed name
    global ainame #stores the randomly choosen name for the ai
    board = [["-","-","-"],["-","-","-"],["-","-","-"]]
    win = ("Tie")
    twoplayer = 2
    movefirst = 1
    computerboard = [[0,1,2],[3,4,5],[6,7,8]]
    player1name=("player1")
    player2name=("player2")
    ainame=("ai")
def printboard(x): #provides an easy way to print the game board without repeating the same print command over and over
    print ("------------Columns------------\n          1    2    3","\n      1",x[0],"\nRows: 2",x[1],"\n      3",x[2],"\n-------------------------------")
def yourturn(x):#allows the user to mark a square.
    global recentturn
    if x == ("X"):
        print("\nit is",player1name+"'s turn") #allows multiple different players to use the same function at the same time
    elif x == ("O"):
        print("\nit is",player2name+"'s turn")
    while True:
        try:
            input1 = int(input("what row is the square you want to mark located in?: "))
            input2 = int(input("what column is the square you want to mark located in?: "))
            if input1 > 0 and input2 > 0 and computerboard[input1-1][input2-1] != 10: #decides if the input is legal or not
                board[input1-1][input2-1] = (x) #stores the input in the physical board
                computerboard[input1-1][input2-1] = 10 #stores the input in the digital board 
                return
            else:
                1/0 #triggers the except clause if the input will not work as it is either already selected or not it the 2d list
        except:
            print ("please only enter a number from 1 to 3 and only select empty boxes")
def computerturneasy(): #allows the computer to move
    print("\nit is",ainame+"'s turn")
    x = random.randint(0,8) #chooses a random number from 0-8
    while x not in computerboard[0] and x not in computerboard[1] and x not in computerboard[2]: #uses the digital board to decipher whether the random number is selected already
        x = random.randint(0,8)
    y = x%3 #finds the column
    x= x//3 #finds the row
    board[x][y] = ("O") #marks the square
    computerboard[x][y] = 10
def wincheck(): #after every turn, this function checks if there is a winner
    global win
    for i in range(3):
        if board[i][0] == board[i][1] and board [i][1] == board[i][2]: # checks if any column has any wins
            if board[i][0] == ("X"):
                win = ("X")
                return
            elif board[i][0] ==("O"):
                win = ("O")
                return
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]: #checks if any row has a win
            if board [0][i] == ("X"):
                win =("X")
                return
            elif board[0][i] == ("O"):
                win = ("O")
                return
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]: #checks if a diagonal has a win
        if board[0][0]==("X"):
            win = ("X")
            return
        elif board[0][0]==("O"):
            win = ("O")
            return
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]: # checks the other diagonal for a win
        if board[1][1]==("X"):
            win = ("X")
            return
        elif board[1][1]==("O"):
            win = ("O")
            return
    return
def playgame(): #combines all functions regarding playing tic tac toe to make the actual game functional
    print("\n\n\n")
    gameendcheck = True
    for i in range(5):
        printboard(board)
        if movefirst == 2 or i > 0 and twoplayer == 2: #checks if two player or allowing the ai to move first has been choosen
            computerturneasy()
            printboard(board) #prints the board after a turn
            wincheck()
            if win == ("X") or win == ("O") and gameendcheck == True: #checks if a win was detected in wincheck
                gameendcheck = False
                gameend()
                return
        if movefirst == 1  or i < 4:
            yourturn("X")
            printboard(board)
            wincheck()
            if win == ("X") or win == ("O") and gameendcheck == True:
                gameendcheck = False
                gameend()
                return
        if twoplayer==1 and i < 4:
            yourturn("O")
            printboard(board)
            wincheck()
            if win == ("X") or win == ("O"):
                gameendcheck = False
                gameend()
                return
        if gameendcheck == True and i == 4: #after the board is full, if a win is still undetected, this will end the function and give a tie
            gameend()
            return
def gameend(): #after playgame finishes, this function runs to see who won
    global player1score
    global player2score
    global aiscore
    recentgames.append([board,win]) #adds the final board and who won to recent games so it can be viewed later
    printboard(board)
    if win == ("X"): #runs if x wins
        print(player1name,"(X) Won The Game!")
        player1score = player1score+1 #adds 1 to x's score
        streak["player1"] = streak["player1"] + 1 #resets all steaks other than player 1's, and adds 1 to player 1's streak
        streak["player2"] = 0
        streak["ai"] = 0
        recentgames[-1].append(player1name) #adds the name of player 1 to the stored game so it can also be viewed in recent games
    elif win ==("O"):
        if twoplayer == 1:#O can be played by the ai, or player 2, so this checks who actually played and won
            print(player2name,"(O) Won The Game!")
            player2score = player2score+1
            streak["player2"] = streak["player2"]+1
            streak["player1"] = 0
            streak["ai"] = 0
            recentgames[-1].append(player2name)
        else:
            print(ainame,"(O) won the game")
            aiscore = aiscore+1
            streak["ai"] = streak["ai"] +1
            streak["player1"] = 0
            streak["player2"] = 0
            recentgames[-1].append(ainame)
    elif win == ("Tie"): 
        print("it's a tie!")
        streak["player2"] = 0 #sets all streaks to zero
        streak["player1"] = 0
        streak["ai"] = 0
        recentgames[-1].append("Unknown") #stores unknown instead of the name of the player who won
def menuprint(): #prints the menu
        print("""\n\n\n-------Menu-------
1) Play Game
2) See Results
3) Exit          
------------------""")
def results(): #runs the result page
    print("\n\n\n")
    try:
        if len(recentgames) > 0:
            for i in range(len(recentgames)):
                printboard(recentgames[i][0])
                print ("Victor:",recentgames[i][1],"\nPlayed by: ",recentgames[i][2]) #prints all previous games, who won, and the name of the winner
            print("\nThe Ai has won",aiscore,"games!")
            print("player 1 has won",player1score,"games!")
            print("player 2 has won",player2score,"games!")
            if streak["player1"] > 0:
                print("Player 1 currently has a streak of",streak["player1"]) #prints who currently has a streak
            elif streak["player2"] > 0:
                print("Player 2 currently has a streak of",streak["player2"])
            elif streak["ai"] > 0:
                print("The Ai currently has a streak of",streak["ai"])
            else:
                print("No streaks in progress")
            input("\nPress the 'enter' key to exit: ")
        else:
            print("you must first play a game to review its results") #runs if the user tries to open the results page before playing a game
    except:
        print("Results page error")
def menu(): #runs the entire game
    while True:
        try:
            menuprint()
            reset()
            input1 = int(input("choose your option (enter a number from 1-3): "))
            if input1 > 0 and input1 < 4:
                if input1 == 1:
                    gamemode()
                    playgame()
                elif input1 == 2:
                    results()
                elif input1 == 3:
                    return
            else:
                print("please only enter a number from 1-3")
        except:
            print("please only enter a number from 1-3 (Error occured)")
def gamemode(): #allows the user to play against an ai or another player
    global twoplayer
    while True:
        try:
            inputa = int(input("Do you want to play against another human (enter 1), or against an Ai (Enter 2)?: "))
            if inputa == 1:
                twoplayer = 1
                entername(2) #allows the user to choose two names
                return
            elif inputa == 2:
                twoplayer = 2
                gofirst()
                entername(1) #allows the user to choose 1 name because the ai gets its name automaticly
                return
            else:
                1/0
        except:
            print("Only enter the number 1 or 2")
def gofirst(): #allows the user to choose whether or not they want to go first
    global movefirst
    while True:
        try:
            inputa = int(input("Do you want to move first (Enter 1), or second (Enter 2)?: "))
            if inputa == 1:
                movefirst = 1
                return
            elif inputa == 2:
                movefirst = 2
                return
            else:
                1/0
        except:
            print("Only enter the number 1 or 2")
def entername(x): #allows the user to enter they're own name
    global player1name
    global player2name
    global ainames
    global ainame
    player1name = input("Enter a name for player 1: ")
    if x == 2:
        player2name = input("Enter a name for player 2: ")
    else:
        ainame = random.choice(ainames) #if the ai is selected, this randomly chooses its name
    return


reset()
othervariables()
menu()
print("Thanks for Playing!")