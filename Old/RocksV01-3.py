# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 23:50:25 2017

@author: T-Dog the Pasta Chef

Simulating the game Arcana, or as we called it "Rocks!"

V01-3
Actually have a working version of the game.

Fix a few issues in terms of interface.  


"""
import os
#import splash
#import time
playSplash = False

scored = True

board = [3,3,3,3,3,3,0,3,3,3,3,3,3,0]

myScore = board[6]
opScore = board[13]

myTurn = False

hand = 0

printScored = False

def getUserInput(board, myTurn):

    inputCorrect = False
    
    while inputCorrect == False:
        
        userInput = int(input('\n\nWhich square to pick up? : '))
        
        if userInput == 55:
            exit()
        
        if userInput == 6 or userInput == 13:
            print('\nOops! You cannot pick up a goal.')
            
        elif myTurn == True and userInput in [7,8,9,10,11,12]:
            
            print('\nYou have to pick up from your own side, dumdum!')
            
        elif myTurn == True and userInput not in [0,1,2,3,4,5]:
            
            print('\nPlease select a square on your side, 0-5')
            
        elif myTurn == False and userInput not in [7,8,9,10,11,12]:
            
            print('\nPlease select a square on their side, 7-12')
            
        elif myTurn == False and userInput in [0,1,2,3,4,5]:
            
            print('\nNice try. Pick up from your own board')
            
        elif board[userInput] == 0:
            
            print('\nYou cannot pick up an empty square. Idiot.')
            
        else:
            inputCorrect = True
            
    return userInput

def printBoard(board, myTurn, scored, printScored,someoneWon):
    
    os.system('cls')   
    
    printOpBoard(board)
    printScores(board)
    printMyBoard(board)   
    
    if myTurn and printScored: 
        
        print('\nYou Scored!')
        
        #printScored = False       
        
    elif not myTurn and printScored:
        
        print('\nOpponent Scores!')
        
        #printScored = False
        
    if myTurn and someoneWon == False:  
        
        print("\nIt's your turn.", end=' ')
        
    elif not myTurn and someoneWon == False:
        
        print("\nIt's their turn.", end=' ')
    
def printOpBoard(board):
    
    opBoard = reversed(board[7:13])
    
    print('\n \n   12   11   10    9    8    7')
    
    print ('  ┌───┐┌───┐┌───┐┌───┐┌───┐┌───┐')
    print('  ', end='')
       
    for place in opBoard:
        
        if place < 10:
        
            print('│ ', end='')
            
            print(str(place) + ' │', end='')
            
        else:
            print('│', end='')
            print(str(place) + ' │', end='')
        
    print('') #start a new line
    
    print('  └───┘└───┘└───┘└───┘└───┘└───┘')
    
def printMyBoard(board):
    
    myBoard = board[0:6]
    
    print('  ╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗')
    print('  ', end='')
    
    for place in myBoard:
        
        if place < 10:
        
            print('║ ', end='')
            
            print(str(place) + ' ║', end='')
            
        else:
            print('║', end='')
            
            print(str(place) + ' ║', end='')
        
    print('') #new line
    print('  ╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝')
    
    print('    0    1    2    3    4    5')
    
def printScores(board):
    
    print('  ╔───╗░░░░░░░░░░░░░░░░░░░░╔«═»╗')
    print('  ', end='')
    
    if board[13] < 10:
    
        print('│ ' + str(board[13]), end='')
        
    else:
        print('│' + str(board[13]), end='')
        
        
    if board[6] < 10:
        
        print(' │░░░░░░░░░░░░░░░░░░░░║ ' + str(board[6]) + ' ║')
        
    else:
        print(' │░░░░░░░░░░░░░░░░░░░░║' + str(board[6]) + ' ║')
        
    
    print('  ╚───╝░░░░░░░░░░░░░░░░░░░░╚«═»╝')
    
def oneTurn(board, hand, myTurn, someoneWon, printScored):
    
    scored = True
    
    def pickUpSquare(board, hand, currentSquare):       
        hand += board[currentSquare]       
        board[currentSquare] = 0
        return board, hand 
    
    def moveSquares(board,hand,currentSquare,myTurn,printScored): # The meat and potot
    
        while hand > 0:
             
            currentSquare += 1
            
            if currentSquare == 14:
                currentSquare = 0
            
            #Check for the easy one score, otherwise keep moving
            if myTurn and currentSquare == 6 and hand == 1:
                
                board[6] += 1
                scored = True 
                hand = 0
                printScored = True
                return board, scored, hand, myTurn, printScored
                
            elif myTurn and currentSquare == 6 and hand > 1:
                currentSquare += 1
                
            elif myTurn and currentSquare == 13:
                continue
                
            elif not myTurn and currentSquare == 6:
                currentSquare += 1
                
            elif not myTurn and currentSquare == 13 and hand > 1:
                currentSquare = 0
                
            elif not myTurn and currentSquare == 13 and hand == 1:            
                board[13] += 1
                scored = True
                hand = 0
                printScored = True
                return board, scored, hand, myTurn, printScored
                
            elif not myTurn and currentSquare == 13 and hand > 1:
                currentSquare +=1 
            
            
            if hand == 1 and board[currentSquare] != 0:
                
                board, hand = pickUpSquare(board, hand, currentSquare)
                
            elif hand == 1 and board[currentSquare] == 0:
                
                board[currentSquare] = 1
                hand = 0 
                
            else:
                
                board[currentSquare] += 1
                    
                hand -= 1
           
        scored = False
        
        if myTurn == True:
            
            myTurn = False
            
        elif myTurn == False:
            myTurn = True
            
        return board, scored, hand, myTurn,printScored
    
    
        
    while scored: # Main turn loop
    
        printBoard(board,myTurn,scored, printScored,someoneWon)
        printScored = False
        
        currentSquare = getUserInput(board, myTurn) 
        
        board, hand = pickUpSquare(board, hand, currentSquare) 
        
        board, scored, hand, myTurn, printScored = moveSquares(board, hand, currentSquare, myTurn,printScored) # Get moving!
        
        if sum(board[0:6]) == 0 or sum(board[7:13]) == 0:
            
            someoneWon = True
    
            return board, myTurn, someoneWon, printScored
    
        elif board[13] == 18 or board[6] == 18:
            
            someoneWon = True
            
            return board, myTurn, someoneWon, printScored
        
    return board, myTurn, someoneWon, printScored
    
def playGame(board, hand, myTurn,scored, playSplash,printScored):
    
    
    if playSplash:
        splash.printBanner()    
        os.system('cls')
    
    
    someoneWon = False
    
    #printBoard(board)
    
    while someoneWon == False:
    
        board, myTurn, someoneWon,printScored = oneTurn(board, hand, myTurn, someoneWon, printScored)       
            
    if board[6] > board[13]:
        printBoard(board,myTurn,scored,printScored,someoneWon)
        print('\nYou won!')       
        
    elif board[13] > board[6]:
        printBoard(board,myTurn,scored,printScored,someoneWon)
        print('\nYour opponent won!')
      
        
    elif board[13] == board[6]:
        printBoard(board,myTurn,scored,printScored,someoneWon)
        print('\nIt was a draw!')
        
        
playGame(board, hand, myTurn, scored, playSplash, printScored)


