import pygame
import os


pieceMoves = {

    "B": 
    {
        "Attack": [],
        "Move": [
                 (1,1), (-1,-1),(-1,1),(1,-1),
                 (2,2),(-2,2),(2,-2),(-2,-2),
                 (3,3),(-3,3),(3,-3),(-3,-3),
                 (4,4),(-4,4),(4,-4),(-4,-4),
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
            (-1,1),(0,-1),],
        "Special": []

    },

    "Q":
    {
        "Attack": [],
        "Move": [
                (1,1), (-1,-1),(-1,1),(1,-1),
                #  (2,2),(-2,2),(2,-2),(-2,-2),
                #  (3,3),(-3,3),(3,-3),(-3,-3),
                #  (4,4),(-4,4),(4,-4),(-4,-4),
                #  (5,5),(-5,5),(-5,-5),(5,-5),
                #  (6,6),(-6,6),(-6,-6),(6,-6),
                #  (7,7),(-7,7),(-7,-7),(7,-7),
                #  (0,1),(-1,0),(0,-1),(1,0),
                #  (0,2),(-2,0),(0,-2),(2,0),
                #  (0,3),(-3,0),(0,-3),(3,0),
                #  (0,4),(-4,0),(0,-4),(4,0),
                #  (0,5),(-5,0),(0,-5),(5,0),
                #  (0,6),(-6,0),(0,-6),(6,0),
                (0,7),(-7,0),(0,-7),(7,0)
    
        ],
        "Special": []

    },

    "N":{
        "Attack": [],
        "Move": [(2,1),(2,-1),
                 (1,2),
                (-2,-1),(-2,1),
                (-1,2),
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
        "Attack": [],
         "Move": [(1,1),(-1,0),(-1,-1),(-1, 1),(0,2),(2,0),(-2,0),(0,-2)],
        "Special": [(-2,0),(2,0)]
    },
    "--":{
        "Attack": [],
        "Move": [],
        "Special": []
    
    }
}
# class FenReader():
#     file = open("RpChess\FEN\FEN1.txt")
#     for file in file():
#         FENboard = file.read()
#         print(FENboard)
#     else:
#         file.close()
#     pass

 
class GameState():
    def __init__(self):
        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bP","bP","bP","bP","bP","bP","bP","bP"],       
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wP","wP","wP","wP","wP","wP","wP","wP"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]
           ]
        
        self.whiteToMove = True
        self.movelog = [] 
    
    def MakeMove(self, move, whiteMove): 
        selecteSqaure = (move.endRow,move.endCol)
        validMove = False
        validPiece = True
        piece = self.board[move.startRow][move.startCol]

        if (whiteMove and piece[0] == 'w') or (not whiteMove and piece[0] == 'b'):
            validPiece = True
        else:
            validMove = False
        print(selecteSqaure)
        if(selecteSqaure and piece[0] == 'b'):
            validMove = False
            print(validMove)

        
            


        ## For move calculation 
        rowChange = move.endRow - move.startRow
        colChange = move.endCol - move.startCol
        changeTuple =  (rowChange, colChange)
        print(changeTuple)

        #Selects the first letter of the piece Object 
        pieceType = piece[1]

        #piece object is checked to see if it is making a valid move or not 
        if changeTuple in pieceMoves[pieceType]["Move"]:
            validMove = True
          
        if validMove and validPiece:
            self.board[move.startRow][move.startCol] = "--"             
            self.board[move.endRow][move.endCol] = piece
            self.movelog.append(move)
            
            return True          
        else:
            return False

class Move():
    def __init__(self, startSq, endSq):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        
    def getChessNotation(self):
        return f"{chr(self.startCol + ord('a'))}{8 - self.startRow}{chr(self.endCol + ord('a'))}{8 - self.endRow}"
     + self.getRankFile(self.endRow, self.endCol)
    
   
        
