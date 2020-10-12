# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 18:50:25 2017

@author: T-Dog the Pasta Chef

Simulating the game Arcana, or as we called it "Rocks!"


"""


board = [3,3,3,3,3,3,0,3,3,3,3,3,3,0]

myScore = board[6]
opScore = board[13]

myTurn = True

hand = 0

def printBoard(board, hand):
    
    printOpBoard(board)
    printScores(board)
    printMyBoard(board)   
    
def printOpBoard(board):
    
    opBoard = reversed(board[7:13])
    
    print('\n \n   12   11   10    9    8    7')
    
    print ('  ┌───┐┌───┐┌───┐┌───┐┌───┐┌───┐')
    print('  ', end='')
       
    for place in opBoard:
        
        print('│ ', end='')
        
        print(str(place) + ' │', end='')
        
    print('') #start a new line
    
    print('  └───┘└───┘└───┘└───┘└───┘└───┘')
    
def printMyBoard(board):
    
    myBoard = board[0:6]
    
    print('  ╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗')
    print('  ', end='')
    
    for place in myBoard:
        
        print('║ ', end='')
        
        print(str(place) + ' ║', end='')
        
    print('') #new line
    print('  ╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝')
    
    print('    0    1    2    3    4    5')
    
def printScores(board):
    
    print('  ╔───╗░░░░░░░░░░░░░░░░░░░░╔«═»╗')
    print('13', end='')
    
    print('│ ' + str(board[13]), end='')
    print(' │░░░░░░░░░░░░░░░░░░░░║ ' + str(board[6]) + ' ║6')
    
    print('  ╚───╝░░░░░░░░░░░░░░░░░░░░╚«═»╝')
    
def oneTurn(board, hand, myTurn):
    
    scored = True
    
    def pickUpSquare(board, hand, currentSquare):       
        hand += board[currentSquare]       
        board[currentSquare] = 0
        return board, hand 

#    def easyOneScore(board, hand):
#
#        if myTurn and currentSquare == 5 and hand == 1:   
#            board[6] += 1
#            hand = 0           
#        if not myTurn and currentSquare == 12 and hand == 1:           
#            board[13] += 1
#            hand = 0           
#        return board, hand # If the preceding conditions aren't met it will just return them
    
    def moveSquares(board,hand,currentSquare,myTurn): # The meat and potot
    
        while hand > 0:
             
            currentSquare += 1
            
            if currentSquare == 14:
                currentSquare = 0
            
            #Check for the easy one score, otherwise keep moving
            if myTurn and currentSquare == 6 and hand == 1:
                
                board[6] += 1
                scored = True 
                hand = 0
                print('You scored!')
                return board, scored, hand
                
            elif myTurn and currentSquare == 6 and hand > 1:
                currentSquare += 1
                
            elif myTurn and currentSquare == 13:
                currentSquare = 0
                
            elif not myTurn and currentSquare == 13 and hand == 1:            
                board[13] += 1
                scored = True
                hand = 0
                print('Op Scored!')
                return board, scored, hand
                
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
                
                printBoard(board,hand)
            
            
            
        scored = False
            
        return board, scored, hand
    
    
        
    while scored: # Main turn loop
        
        currentSquare = int(input('Which to pick up: ')) #TODO need to limit the input for correct player side 
        
        #printBoard(board,hand)
        
        board, hand = pickUpSquare(board, hand, currentSquare) 
        
        #printBoard(board, hand)
        
        #board, hand = easyOneScore(board, hand) #Check to see if the picked up a one next to the goal
        
        board, scored, hand = moveSquares(board, hand, currentSquare, myTurn) # Get moving!
        printBoard(board,hand)
    
        
    return board
    
printBoard(board, hand)

#print('\nCurrent hand has ' + str(hand) + ' rocks.')

board = oneTurn(board, hand, myTurn)

printBoard(board, hand)
