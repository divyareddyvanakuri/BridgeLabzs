import random
def whogofirst():
    if random.randint(0,1)==0:
        return 'computer'
    else:
        return 'player'
def theboard(board):
    print("%c  | %c |%c"%(board[1],board[2],board[3]))
    print("---|---|---")
    print("%c  | %c |%c"%(board[4],board[5],board[6]))
    print("---|---|---")
    print("%c  | %c |%c"%(board[7],board[8],board[9]))
def CheckPosition(x):    
    if(board[x] == ' '):    
        return True
    else:
        print("shell was not empty,so please enter another position value to move forward")
        return False
def isWinner(bo,le):
    return ((bo[1]==le and bo[2]==le and bo[3]==le) or
        (bo[4]==le and bo[5]==le and bo[6]==le) or
        (bo[7]==le and bo[8]==le and bo[9]==le) or
        (bo[1]==le and bo[5]==le and bo[9]==le) or
        (bo[3]==le and bo[5]==le and bo[7]==le) or
        (bo[1]==le and bo[4]==le and bo[7]==le) or
        (bo[2]==le and bo[5]==le and bo[8]==le) or
        (bo[3]==le and bo[6]==le and bo[9]==le))
def isboardfull(board):
    #if (board[1]!=" " and board[2]!=" " and board[3]!=" " and board[4]!=" " and board[5]!=" " and board[6]!=" " and 
        #board[7]!=" " and  board[8]!=" " and board[9]!=" "):
    for i in range(1,10):
        if (board[i] == " "):
            return False
    return True
def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')
print("||TIC.....TAC.....TOE||")
while True:
    board = [" "]*10
    turn = whogofirst()
    gameIsPlaying=True
    while gameIsPlaying:
        if turn=="computer":
            print("computer")
            mark = "x"
            choice = int(input("enter position between [1-9]:"))
            if (CheckPosition(choice)):
                board[choice] = mark
                if (isWinner(board, mark)):
                    theboard(board)
                    print("computer won th game!")
                    gameIsPlaying = False
                else:
                    if isboardfull(board):
                        theboard(board)
                        print("game is tie")
                        break
                    else:
                        turn = "player"
        else:
            print("player")
            mark = "o"
            choice = int(input("enter position between [1-9]:"))
            if (CheckPosition(choice)):
                board[choice] = mark
                if (isWinner(board, mark)):
                    theboard(board)
                    print("player won game!")
                    gameIsPlaying = False
                else:
                    if isboardfull(board):
                        theboard(board)
                        print("game is tie")
                        break
                    else:
                        turn = "computer"
            
    if not playAgain():
        break