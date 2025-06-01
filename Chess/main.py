import pygame as py
import ChessEngine
import chess

py.init()

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT//DIMENSION
FPS = 30


IMAGES= {}


def loadImage():
    pieces = ["wR","wN","wB","wQ","wK","wP","bR","bN","bB","bQ","bK","bP"]
    for piece in pieces:
        IMAGES[piece] = py.transform.scale(py.image.load("ImageFile\PieceImage/" + piece + '.png'),(SQ_SIZE,SQ_SIZE))
        

      
 
def main():
    SelectedX = -1
    SelectedY = -1 
    selectedPiece = False
    whiteMove = True


    py.display.set_caption("RPchess")
    window = py.display.set_mode((WIDTH,HEIGHT))
    clock = py.time.Clock()
    window.fill("white")
    gs = ChessEngine.GameState()
    loadImage()

    run = True

    while run:

        drawGameState(window,gs)
        for e in py.event.get():
            if e.type == py.QUIT:
                run = False
            
            elif e.type == py.MOUSEBUTTONDOWN:

                mx,my= py.mouse.get_pos()
                row = my
                col = mx

                col = int(col/64)
                row = int(row/64)
                print(row,col)

                if selectedPiece:
                    move = ChessEngine.Move([SelectedY, SelectedX], [row, col])
                    if gs.MakeMove(move, gs.whiteToMove):
                        gs.whiteToMove = not gs.whiteToMove

                    selectedPiece = False
                        
                else:
                    selectedPiece = True
                    SelectedX = col
                    SelectedY = row
                    
                        

        clock.tick(FPS)
        py.display.flip()
    


def drawGameState(window,gs):
    drawBoard(window)
    drawPiece(window,gs.board)
    


def drawBoard(window):
    colors = [py.Color("white"), py.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) %2)]
            py.draw.rect(window, color, py.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
            
    

def drawPiece(window,board):
    
    for r in range(DIMENSION):
        for c in range(DIMENSION):     
            if board[r][c] != "--":
                piece = IMAGES[board[r][c]]
                window.blit(piece, (c*SQ_SIZE, r*SQ_SIZE))
         





if __name__ == "__main__":
    main()
