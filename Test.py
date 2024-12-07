board = [["X","X","X"],["X","X","-"],["X","-","X"]]
input1 = 1
input2 = 2
player1name= ("JERRY")
computerboard = [[0,1,2],[3,4,5],[6,7,8]]
recentgames =[]
player2name = ("Andrew")

def printboard(x):
    print ("------------Columns------------\n          1    2    3","\n      1",x[0],"\nRows: 2",x[1],"\n      3",x[2],"\n-------------------------------")
def computerturnhard():
    global mustgo
    if 4 in computerboard:
        board[1][1] = ("O")
        computerboard[1][1] = 90
    if mustgo[0] != 5:
        if mustgo[1]==1:
            for i in range(9):
                if i in computerboard[mustgo[0]]:
                    x = computerboard.index(i)
                    computerboard[mustgo[0]][x] = 90
                    board[mustgo[0]][x] = ("O")
        if mustgo[1]==2:
            for i in range(9):
                if i in computerboard[0][mustgo]:
                    x = computerboard.index
                if i in computerboard[1][mustgo]:
                    print("l")
                if i in computerboard[2][mustgo]:
                    print("l")
def twocornercheck():
    for i in range(3):
        if computerboard[i][1]+computerboard[i][0]+computerboard[i][2] > 28 and computerboard[i][1]+computerboard[i][0]+computerboard[i][2] < 50:
            mustgo = [i,1]
            return
        elif computerboard[0][i]+computerboard[1][i]+computerboard[2][i] > 28 and computerboard[0][i]+computerboard[1][i]+computerboard[2][i] < 50:
            mustgo = [i,2]
            return
        elif computerboard[i][1]+computerboard[i][0]+computerboard[i][2] > 178 and computerboard[i][1]+computerboard[i][0]+computerboard[i][2] < 195:
            mustgo = [i,1]
            return
        elif computerboard[0][i]+computerboard[1][i]+computerboard[2][i] > 178 and computerboard[0][i]+computerboard[1][i]+computerboard[2][i] < 195:
            mustgo = [i,2]
            return
    mustgo =[5,5]
    return


import statistics
DICKtionary = {"Ian":30,"Ibrahim":30,"Jack":39}
dictionary = {"Ian":[30,24,25]}
(list(dictionary.values()))
print(len(DICKtionary))
t = {}
print(len(t))