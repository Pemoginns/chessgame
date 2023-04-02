import pygame as py
import engine
import asyncio
import time
import webbrowser

 
py.init()
WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = 512/8
FPS = 30
SelectedX = -1
SelectedY = -1 
selectedPiece = False
whiteMove = True
highlightedboxes = []
IMAGES= {}
movelog ={}

 
def loadImage():
    pieces = ["R","N","B","Q","K","P","r","n","b","q","k","p"]
    for piece in pieces:
        IMAGES[piece] = py.transform.scale(py.image.load("PieceImage/" + ConvertFENtoIMG(piece) + '.png'),(SQ_SIZE,SQ_SIZE))
        

def ConvertFENtoIMG(f):
    if str(f).isupper():
        return "w" + str(f)         
    else:
        return "b" + str(f)



async def main():
    global selectedPiece
    global SelectedX
    global SelectedY
    global whiteMove


    py.display.set_caption("PuzzelChess")
    window = py.display.set_mode((WIDTH,HEIGHT))
    clock = py.time.Clock()
    window.fill("white")
    gs = engine.GameState()
    loadImage()
    gs.FENBoard()

    run = True
    button = True
   
    

    while run:   
        

        drawGameState(window,gs)
      


        ##functional 
        for e in py.event.get():
            if e.type == py.QUIT:
                run = False
            elif e.type == py.KEYDOWN:
                if  e.key == py.K_d:
                    gs.FENBoard()
                if e.type == py.K_r:
                    review()
            elif e.type == py.MOUSEBUTTONDOWN:
            

                mx,my= py.mouse.get_pos()
                row = my
                col = mx

                col = int(col/64)
                row = int(row/64)
               
           
                if selectedPiece:
               
                    move = engine.Move([SelectedY, SelectedX], [row, col])
                    if gs.MakeMove(move, whiteMove):
                        whiteMove = not whiteMove

                    selectedPiece = False
                        
                else:
                    selectedPiece = True
                    SelectedX = col
                    SelectedY = row

                
           
                
                    
                        

        clock.tick(FPS)
        py.display.flip()
        await asyncio.sleep(0)

def button(window):
     button = True
     
     py.draw.rect((window), "white", py.Rect(SQ_SIZE,SQ_SIZE,64,64))
 
def review():
    url= ["Users\pguin\Desktop\Chessgame\Review.htm"]
    for i in url:
        webbrowser.open(url)
##Functional 
def drawGameState(window,gs):
    drawBoard(window)
    drawhighlight(window, gs.board)
    drawPiece(window,gs.board)
    button(window)
    
##non functional
def drawhighlight(window, board):
    global selectedPiece
    global SelectedX
    global SelectedY
    highlightedboxes = []   
    if selectedPiece:
        yellow = (255,255,0,50)
        red = (255,0,0)
        piece = board[SelectedY][SelectedX]
        movement = engine.GameState.getPieceAttibutes(piece)
        # print(movement)
        for r in range(DIMENSION):
            for c in range(DIMENSION):
                if not piece.islower():
                    if not piece[0] == 'b':
                        for move in movement["Attack"] or movement["Move"]:
                            if SelectedY + move[0] == r and SelectedX + move[1] == c:

                                highlightedboxes.append((r,c))
                                py.draw.rect((window), yellow, py.Rect(c*SQ_SIZE,r*SQ_SIZE,64,64))
                    # for i in highlightedboxes:
                #        pass      


#functional 
def drawBoard(window):
    GREEN = (50,25,120)
    BLACK =(0,0,0)
    colors = [py.Color("white"), py.Color("grey")]

    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) %2)]
            py.draw.rect((window), color, py.Rect(c*SQ_SIZE,r*SQ_SIZE,256,256))
                   
#functional 
def drawPiece(window,board):
    
    for r in range(DIMENSION):
        for c in range(DIMENSION):     
            if board[c][r] != "--":
                piece = IMAGES[board[c][r]]
                window.blit(piece, (r*SQ_SIZE, c*SQ_SIZE, SQ_SIZE, SQ_SIZE))

#functional        
if __name__ == "__main__":
    asyncio.run(main())
   