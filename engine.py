##for sound function
import pygame as py
import os
from pygame import mixer
import random 


mixer.init()
moveSound = py.mixer.Sound('MoveSound.wav')
clickSound = py.mixer.Sound('ClickSound.wav')




pieceMoves = {
    

    "B": 
    {
        "Attack": [],
        "Move": [
                 (1,1), (-1,-1),(-1,1),(1,-1),
                 (2,2),(-2,2),(2,-2),(-2,-2),
                 (3,3),(-3,3),(3,-3),(-3,-3),
                 (4,4),(-4,4),(-4,-4),(4,4),
                 (5,5),(-5,5),(-5,-5),(5,-5),
                 (6,6),(-6,6),(-6,-6),(6,-6),
                 (7,7),(-7,7),(-7,-7),(7,-7),
                 ]
    },



    "K":
    {
        "Attack": [],
        "Move": [
            (1,1),(-1,-1),
            (1,0),(0,1),
            (-1,0),(0,-1),
            (-1,1),(0,-1),(-1,-1),],
        "Special": [],
        "Castle": [(-3,0),(0,3)]

    },
    'p':
    {
        "Attack":[],
        "Move":[],
        "Enpassant":[],
    },
     'r':
    {
        "Attack":[],
        "Move":[],  
    },
     'b':
    {
        "Attack":[],
        "Move":[],
    
    },
     'k':
    {
        "Attack":[],
        "Move":[],
    
    },
     'q':
    {
        "Attack":[],
        "Move":[],  
    
    },
     'n':
    {   
        "Attack":[],
        "Move":[],
    },


    "Q":
    {
        "Attack": [],
        "Move": [
                (1,1), (-1,-1),(-1,1),(1,-1),
                 (2,2),(-2,2),(2,-2),(-2,-2),
                 (3,3),(-3,3),(3,-3),(-3,-3),
                 (4,4),(-4,4),(-4,-4),(4,4),
                 (5,5),(-5,5),(-5,-5),(5,-5),
                 (6,6),(-6,6),(-6,-6),(6,-6),
                 (7,7),(-7,7),(-7,-7),(7,-7),
                 (0,1),(-1,0),(0,-1),(1,0),
                 (0,2),(-2,0),(0,-2),(2,0),
                 (0,3),(-3,0),(0,-3),(3,0),
                 (0,4),(-4,0),(0,-4),(4,0),
                 (0,5),(-5,0),(0,-5),(5,0),
                 (0,6),(-6,0),(0,-6),(6,0),
                 (0,7),(-7,0),(0,-7),(7,0)
    
        ],
        "Special": []

    },



    
        "N":{
            "Attack": [],
            "Move": [(2,1),(2,-1),
                    (1,2),
                    (-2,-1),(-2,1),
                    (-1,2),(-1, 2),
                    (1,-2),(-1,-2)],
            "Special": []

        },


    "R" :
    {
        "Attack": [],
        "Move": [(0,1),(-1,0),(0,-1),(1,0),
                 (0,2),(-2,0),(0,-2),(2,0),
                 (0,3),(-3,0),(0,-3),(3,0),
                 (0,4),(-4,0),(0,-4),(4,0),
                 (0,5),(-5,0),(0,-5),(5,0),
                 (0,6),(-6,0),(0,-6),(6,0),
                 (0,7),(-7,0),(0,-7),(7,0)],
        "Special": []
    },
 
    "P":{
        "Attack": [(-1,1),(-1,-1)],
        "Move": [(-1,0),(-1,-1),(-1, 1)],
        "Special": [(-2,0),(2,0)],
        "Enpassant": [(-2,-1), (-2,1)]
    },
   
    "-" :{
        "Attack": [],
        "Move": [],
        "Special": []
    },
    "--":{
        "Attack": [],
        "Move": [],
        "Special": []
    
    } 
}

## mate check 
## sound and audio 
## movement position check
## Moving through pieces
##music calcuations

##FEN change check 
##Fix the movement

#functional
class Move():
    def __init__(self, startSq, endSq):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
             

#functional
class GameState():
    feni = 1
    checkmate = False
    
    
    def __init__(self):
        pass
    ##functional
    def MakeMove(self, move, whiteMove): 
        
        
        validMove = True
        validPiece = True  
        whiteMove = False
        CastleMove = True
        Enpassant = False
     
   

        SelectedPiece = (move.startRow, move.startCol)
        print(SelectedPiece, "SelectedPiece")

        selectedSqaure = (move.endRow,move.endCol)  
        print("Select Square",selectedSqaure)

        piece = self.board[move.startRow][move.startCol]
  
        ## For move calculation 
        rowChange = move.endRow - move.startRow
        colChange = move.endCol - move.startCol
        changeTuple =  (rowChange, colChange)
        
        occupied = piece
        
        print("ChangeTuple:" , changeTuple)

        # Selects the first letter of the piece Object 
        pieceType = piece[0]
        if selectedSqaure != "--":
            validMove = False
        if SelectedPiece and piece[0] == 'b':
            validMove = False

        ##allows the white pieces to move
        if(whiteMove == False and piece[0] == 'b'):
            validMove = True
            
        #piece object is checked to see if it is making a valid move or not 

        if changeTuple in pieceMoves[pieceType]["Move"]:
            validMove = True
        # if changeTuple in pieceMoves[pieceType]["Castle"]:
        #     if piece[0] == 'k' or piece[0] == 'K':
        #         validMove = True
        #         CastleMove = True 

        if piece[0] =='K' and CastleMove:

            if CastleMove and move.endRow and move.endCol:             
                if piece[0] == 'R' or 'r':
                    print("Castle Attempted")                                  
        else:
            CastleMove = False  

        #non functional 
        if piece[0] == 'P' and Enpassant:      
            ##needs a new variable to define that piece that is being removed    
            if changeTuple in pieceMoves[pieceType]["Enpassant"] and piece[0] == 'P':
                if piece[0] == 'p':
                    (print("remove black"))      
                print("Enpassant = ",  move.endRow + 1, move.endCol)
                validMove = True



        #functional   
        if validMove and validPiece:
            clickSound.play()
            self.board[move.startRow][move.startCol] = "--"             
            self.board[move.endRow][move.endCol] = piece
                  
            
            return True          
        else:
            return False

    #functional

      
            
            # print("Checkmate")
    ##make the game iterate through FENS on Checkmate
    #functional



    def FENBoard(self):
        checkmate = False

        fen = randint = random.randint(1,16)
        # fen = 16
  
        print("You are on puzzle ", fen)
        
        self.board = [
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],       
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"]
           ]
        
        fenlist = ["FEN/FEN1.txt", "FEN/FEN2.txt","FEN/FEN3.txt", "FEN/FEN1.txt","FEN/FEN4.txt",
                   "FEN/FEN5.txt", "FEN/FEN6.txt","FEN/FEN7.txt","FEN/FEN8.txt","FEN/FEN9.txt",
                   "FEN/FEN10.txt","FEN/FEN11.txt","FEN/FEN12.txt", "FEN/FEN13.txt","FEN/FEN14.txt",
                   "FEN/FEN15.txt","FEN/FEN16.txt"]   
    
        currentFen = fenlist[fen]
        Fenfile = open(currentFen,"r")
        FenDiv = Fenfile.read()  
        Fenbreak = FenDiv.split("/")

        x = 0 
        if fen: 
            checkmate = False
            if not checkmate:
                for i in self.board:
                    for j in i:
                        if  j != 'k':
                            checkmate = True
                            
                    
                   
            else: checkmate = False  
                            
            for row in Fenbreak:
                y = 0     
                for i in row:
                    if(i.isdigit()):
                        e = y
                        while e < (y + int(i)):
                            self.board[x][y] = "--"
                            e += 1
                        y += int(i)                                          
                    else:   
                        self.board[x][y] = i
                        y += 1                 
                x += 1
             
      

        # print(self.board)

    #non functional
    def getPieceAttibutes(piece):
        return pieceMoves[piece]


   
 
        # currentPos = [move.startRow,move.startCol]
        # endPos = [move.endRow, move.endCol]
        

        # rowMove = 1
        # colMove = 1
        # # if currentPos[1] == endPos[1]:
        # #     validMove = True
        # #     print("cp = ep")
        # if currentPos[0] > endPos[0]:
        #     rowMove = -1
        #     currentPos[0] -= 1
        # else: 
        #     currentPos[0] +=1       
        # if currentPos[1] > endPos[1]:
        #     colMove = -1
        #     currentPos[1] -=1
        # else:
        #     currentPos[1] += 1

        
        # for row in range(currentPos[0], endPos[1], rowMove):
        #     for i in occupied:
        #         if occupied:
        #             validMove = False
        #             print(occupied)
        #         print("Check pos("+str(currentPos[0])+", "+str(currentPos[1])+") is occupied")
        #         print(currentPos[0])
        #         print(currentPos[1])
        #         currentPos[0] += rowMove
        #         currentPos[1] += colMove
        

        ##mateCheck
        # if endPos[1] and endPos[0] == piece[0] =='k':
        #     checkmate = True 
        #     print("checkmate")


        ##calste check

        #non functional
  
    


  
