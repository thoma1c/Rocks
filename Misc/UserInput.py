# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 15:35:46 2017

@author: Owner
"""

myTurn = True

board = [0,3,3,3,3,3,0,3,3,3,3,3,3,0]

def getUserInput(board, myTurn):

    inputCorrect = False
    
    while inputCorrect == False:
        
        userInput = int(input('Which square to pick up? : '))
        
        if userInput == 6 or userInput == 13:
            print('\nOops! You cannot pick up a goal.')
            
        elif myTurn == True and userInput in [7,8,9,10,11,12]:
            
            print('\nYou have to pick up from your own side, dumdum!')
            
        elif myTurn == True and userInput not in [0,1,2,3,4,5]:
            
            print('\nPlease select a square on your side, 0-5')
            
        elif myTurn == False and userInput not in [7,8,9,10,11,12]:
            
            print('\nPlease select a square on your side, 7-12')
            
        elif myTurn == False and userInput in [0,1,2,3,4,5]:
            
            print('\nNice try. Pick up from your own board')
            
        elif board[userInput] == 0:
            
            print('\nYou cannot pick up an empty square. Idiot.')
            
        else:
            inputCorrect = True
            
    return userInput
    
currentSquare = getUserInput(board, myTurn)

print('\nThe user selected ', currentSquare)