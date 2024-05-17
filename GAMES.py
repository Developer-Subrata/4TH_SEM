import random
import os
from maskpass import advpass
#import getpass

game=int(input("\n1>> For TIC TAC TOE\n2>> For ROCK PAPER SCISSOR\n3>> For FLAMES\n0>> For EXIT\n===>> "))
if game == 2:
    os.system('cls')
    print("\t*** Now You Are Playing (Rock Paper Scissor) Game ***\n")
    while True:
        def ggg():
            os.system('cls')  
            print("\t*** Now You Are Playing (Rock Paper Scissor) Game ***\n")
        lst = ["rock", "paper", "scissors"]
        user1 = advpass("USER[1]:\nEnter Your Turn (rock, paper, scissors): ").lower() 
        user2 = advpass("USER[2]:\nEnter Your Turn (rock, paper, scissors): ").lower()
        #user1 = getpass("USER[1]:\nEnter Your Turn (rock, paper, scissors): ").lower() 
        #user2 = getpass("USER[2]:\nEnter Your Turn (rock, paper, scissors): ").lower()

        if user1 == user2:
            os.system('cls')
            print("Game Is Tie !!!")
            input()
            ex=input("Do You Want To Exit? [Y/N]").upper()
            if ex=='Y':
                os._exit(os.X_OK)
            else:
                ggg()
        elif (user1 == 'rock' and user2 == 'scissors') or (user1 == 'paper' and user2 == 'rock') or (user1 == 'scissors' and user2 == 'paper'):
            os.system('cls')
            print("Player 1 Won !!!")
            input()
            ex=input("Do You Want To Exit? [Y/N]").upper()
            if ex=='Y':
                os._exit(os.X_OK)
            else:
                ggg()
        else:
            os.system('cls')
            print("Player 2 Won !!!")
            input()
            ex=input("Do You Want To Exit? [Y/N]").upper()
            if ex=='Y':
                os._exit(os.X_OK)
            else:
                ggg()


                    ##########################__TIC ** TAC ** TOE__#####################
elif game == 1:
    os.system('cls')
    print("\t*** Now You Are Playing (TIC_TAC_TOE) Game ***\n")
    while True:
        def ggg():
            os.system('cls') 
            print("\t*** Now You Are Playing (TIC_TAC_TOE) Game ***\n")
        vs=input("C>> PlayWithComputer\tP>> PlayWithFriends\n===>> ").upper()
        board = ["_" for _ in range(9)]             #creation of the board
        currentPlayer = "X"
        gameRunning = True

# Printing the game board
        def printBoard(board):
            print(board[0] + "|" + board[1] + "|" + board[2])
            print(board[3] + "|" + board[4] + "|" + board[5])
            print(board[6] + "|" + board[7] + "|" + board[8])

# Take Player Input
        def playerInput(board):
            while True:
                    inp = int(input("Player 1: \nEnter Your Position (1-9): "))
                    if inp >= 1 and inp <= 9 and board[inp - 1] == "_":
                        board[inp - 1] = currentPlayer
                        break
                    else:
                        print("Invalid input or position already occupied. Try again.")

# Computer Move
        if vs=='C':
            def computer(board):            #if play with computer
                while True:
                    position = random.randint(0, 8)
                    if board[position] == "_":
                        board[position] = "O"
                        break
        elif vs=='P':
            def computer(board):            #if play with other players
                while True:
                    inp = int(input("Player 2: \nEnter Your Position (1-9): "))
                    if inp >= 1 and inp <= 9 and board[inp - 1] == "_":
                        board[inp - 1] = currentPlayer
                        break
                    else:
                        print("Invalid input or position already occupied. Try again.")
        else:
            print("Invalid input . Try again.")
            input()

# Switch Player
        def switchPlayer():
            global currentPlayer
            currentPlayer = "O" if currentPlayer == "X" else "X"

# Check for Win
        def checkWin(board):
            for i in range(3):
                if board[i] == board[i + 3] == board[i + 6] != "_":              # Vertical win
                    return True
                if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] != "_":  # Horizontal win
                    return True
            if board[0] == board[4] == board[8] != "_":                          # Right_Diagonal win
                return True
            if board[2] == board[4] == board[6] != "_":                          # Left_Diagonal win
                return True
            return False
#Check Tie
        def checkTie(board):
            return "_" not in board

        while gameRunning:
            os.system('cls')
            printBoard(board)
            playerInput(board)
            os.system('cls')
            printBoard(board)
            if checkWin(board):
                os.system('cls')
                printBoard(board)
                print(f"Player {currentPlayer} wins!")
                
                ex=input("Do You Want To Exit? [Y/N]").upper()
                if ex=='Y':
                    os._exit(os.X_OK)
                else:
                    ggg()
                    break

            if checkTie(board):
                os.system('cls')
                printBoard(board)
                print("It's a tie!")
                
                ex=input("Do You Want To Exit? [Y/N]").upper()
                if ex=='Y':
                    os._exit(os.X_OK)
                else:
                    ggg()
                    break
                
            switchPlayer()
            computer(board)
            if checkWin(board):
                os.system('cls')
                printBoard(board)
                print(f"Player {currentPlayer} wins!")
                
                ex=input("Do You Want To Exit? [Y/N]").upper()
                if ex=='Y':
                    os._exit(os.X_OK)
                else:
                    ggg()
                    break
                
            if checkTie(board):
                os.system('cls')
                printBoard(board)
                print("It's a tie!")
                
                ex=input("Do You Want To Exit? [Y/N]").upper()
                if ex=='Y':
                    os._exit(os.X_OK)
                else:
                    ggg()
                    break
                
            switchPlayer()

##############################***F-L-A-M-E-S***##########################
if game == 3:
    os.system('cls')
    print("\t*** Now You Are Playing (F-L-A-M-E-S) Game ***\n")
    while True:
        def ggg():
            os.system('cls')  
            print("\t*** Now You Are Playing (F-L-A-M-E-S) Game ***\n")
        name11 = input("Enter Name _1:").upper()
        name22 = input("Enter Name _2:").upper()

        name1 = list(name11)
        name2 = list(name22)
        dup_lst=[]

        for char in name1:
            if char in name2:
                name2.remove(char)
            else:
                dup_lst.append(char)
    
        for char in name2:
            if char in name1:
                name1.remove(char)
            else:
                dup_lst.append(char)
    
        d_ln=len(dup_lst)
        print("Remaining UnMatched Characters : ",dup_lst,"\nIts Length Is: ",d_ln)

        if d_ln>0:
            flames = {'F': "FRIENDSHIP", 'L': "LOVE", 'A': "AFFECTION", 'M': "MARRIAGE", 'E': "ENEMY", 'S': "SIBLINGS"}
            lst = ['F', 'L', 'A', 'M', 'E', 'S']
            while len(lst) > 1:
                remove_index = (d_ln % len(lst) - 1)
                if remove_index >= 0:
                    right = lst[remove_index + 1:]
                    left = lst[: remove_index]
                    lst = right + left
                else:
                    lst = lst[: len(lst) - 1]
            relationship = flames[lst[0]]
            print(f"Relationship For *{name11}* & *{name22}* Is :", relationship)

            input()
            os.system('cls')
            ex=input("Do You Want To Exit? [Y/N]").upper()
            if ex=='Y':
                os._exit(os.X_OK)
            else:
                ggg()
        else:
            print("There Is No Unique Character !!!")
            input()
            os.system('cls')
            ex=input("Do You Want To Exit? [Y/N]").upper()
            if ex=='Y':
                os._exit(os.X_OK)
            else:
                ggg()

elif game==0:
    os._exit(os.X_OK)


#by STR

 
