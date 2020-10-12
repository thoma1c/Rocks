# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 17:07:12 2017

@author: Owner

testing out the game mechanic
"""

board = [3,3,3,3,3,3,0,3,3,3,3,3,3,0]
goals = [0,1,2,3,4,5,6,7,8,9,0,1,2,3]

myScore = board[6]
opScore = board[13]

def printBoard():

    print('\nCurrent Board:')
    
    for space in board:
    
        print(space, end=' ')
        
    print('\n- - - - - - M - - - - - - O')
    print  ('0 1 2 3 4 5 6 7 8 9 10111213')
        
    print('\nMy Score: ', myScore)
    print('Opponent Score: ', opScore)
    
def printMyBoard(): 
    
    print('\nmyBoard:')

    for square in board[0:7]:
        print(square, end=' ')
    
#printBoard()

#playerChoice = input('Pick a place: ')

# Main Game Loop?   

playerChoice = 5
hand = board[playerChoice]
currentSquare = playerChoice
board[currentSquare] = 0
currentSquare += 1

print(board)

myTurn = True

while hand != 0: 

    #print( '',board,'\n',goals)   
    
    if hand == 1 and currentSquare == 6 and myTurn:
        
        board[6] += 1 # I get a point!
        hand = 0        
        print('I score!')
        
    elif hand == 1 and currentSquare == 13 and not myTurn:
        
        board[13] += 1
        hand = 0        
        print('Op Scores.')
        
    elif currentSquare == 6 and hand > 1:
        
        currentSquare += 1
        
    elif board[currentSquare] != 0 and hand > 1:       
  
        board[currentSquare] += 1  
        hand -= 1   
        currentSquare += 1
        
    elif board[currentSquare] != 0 and hand == 1:
        
        hand += board[currentSquare]
        board[currentSquare] = 0
        currentSquare += 1
        
    elif board[currentSquare] == 0 and hand == 1:
        board[currentSquare] = 1
        
    elif hand == 1 and board[currentSquare] == 0:
        board[currentSquare] += 1
        hand -= 1
        
    elif hand == 1 and board[currentSquare] != 0:
        
        hand += board[currentSquare]
        board[currentSquare] = 0
        currentSquare += 1
        
#    Keep going round and round!     
    if currentSquare == 14:
        currentSquare = 0
        
    print(board)
        
#    elif hand == 1 and currentSquare == 10:
#        
#        board[13] += 1 # opponent gets a point
#        hand
#        
#    else:
#        currentSquare += 1
     
        
#    # One has to land exactly on their home base to score, otherwise skip over it    
#    if currentSquare == 6 or currentSquare and hand != 1:
#        currentSquare += 1
        
        


    
        



