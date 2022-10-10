import pygame
import sys
pygame.init()
color = {"WHITE":(255,255,255),"BLACK":(0,0,0),"CYAN":(2, 201, 232),"RED":(235, 64, 52),"BLUE":(8,39,245),"GRAY":(219, 219, 219)}

if len(sys.argv) != 4:
    print("\n[### ERROR ###]\n  Open the file with the following command:\n     python n_tic_tac_toe.py [width] [height] [number to do line]\n")
    sys.exit()
#@@@@@  editables
cols=int(sys.argv[1])
rows=int(sys.argv[2])
n_line=int(sys.argv[3])
token_radius=17
#@@@@@@

window_width=600
window_height=700
board_width=600
board_height=500
window = pygame.display.set_mode((window_width,window_height))
gameFinished=False

player_won=-1

board=[]
for row in range(rows):
    _fila=[]
    for column in range(cols):
        _fila.append(0)
    board.append(_fila)

spaceX = board_width/cols
spaceY = board_height/rows

active=True
window.fill(color['GRAY'])

def rectangulo(coordinates, ancho, alto):
    return pygame.Rect(coordinates[0]-int(ancho/2),coordinates[1]-int(alto/2), ancho, alto)
def drawCloseButton():
    global button_closeRECT
    pygame.draw.rect(window, color['RED'], button_closeRECT)
    print_text("Close game",(board_width/2,window_height-50),15)

def clear():
    window.fill(color['GRAY'])
def printPlayer(nPlayer, coordinates, textSize):
    colorr=color['BLACK']
    if nPlayer==1: 
        nPlayer_text = "RED"
        colorr=color['RED']
    elif nPlayer==2:
        nPlayer_text = "BLUE"
        colorr=color['CYAN']
    fuente = pygame.font.SysFont("Consolas", textSize)
    text_to_show = fuente.render("{0}".format(nPlayer_text), 1, colorr)
    coordinates = text_to_show.get_rect(center=(coordinates[0],coordinates[1]))
    window.blit(text_to_show, coordinates)

def print_text(texto, coordinates, textSize):
    colorr=color['BLACK']
    fuente = pygame.font.SysFont("Consolas", textSize)
    text_to_show = fuente.render("{0}".format(texto), 1, colorr)
    coordinates = text_to_show.get_rect(center=(coordinates[0],coordinates[1]))
    window.blit(text_to_show, coordinates)

def addStep(nPlayer,column):
    #print(f"Paso a column:{column}")
    if holeInColumn(column) is True:
        print(f"pos_to_place:{positionToPlace(column)-1}, {column-1}")
        board[positionToPlace(column)-1][column-1] = nPlayer
        printBoardOnConsole()
        return True
    else:
        print("Tokencan't be placed in that column..")
        return False

def endGame(nPlayer):
    global gameFinished, player_won
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@ LINE @@@@@@@@@@@@@@@@@@@@@@@@@@")
    gameFinished=True
    player_won=nPlayer

def isThereLine():
    global jugadorWin
    cH  = checkHorizontals()
    cV  = checkVerticals()
    cD1 = checkDiagonal1()
    cD2 = checkDiagonal2()

    if cH!=-1:
        endGame(cH)
    elif cV!=-1:
        endGame(cV)
    elif cD1!=-1:
        endGame(cD1)
    elif cD2!=-1:
        endGame(cD2)
    else:
        return False

def checkHorizontals():
    for player in range(1,3):
        for row in range(rows):
            for i in range(cols):
                cant=0
                if not(i + (n_line-1) > (cols-1)): 
                    #print("Comprobando##")
                    for j in range(n_line):
                        #print(f"    {board[row][i+j]}")
                        if board[row][i+j]==player:
                            cant+=1
                    if cant == n_line:
                        return player
    return -1
def checkVerticals():
    for player in range(1,3):
        for col in range(cols):
            for i in range(rows):
                cant=0
                if not(i + (n_line-1) > (rows-1)): 
                    #print("Comprobando##")
                    for j in range(n_line):
                        #print(f"    {board[i+j][col]}")
                        if board[i+j][col]==player:
                            cant+=1
                    if cant == n_line:
                        return player
    return -1
def checkDiagonal1():
    for player in range(1,3):
        for col in range(cols):
            if not(col + (n_line-1)>(cols-1)):
                for row in range(rows):
                    if not(row + (n_line-1)>(rows-1)):
                        for h in range(0,n_line):
                            cant=0
                            #print("Comprobando##")
                            for v in range(0,n_line):
                                if not((row+v)>(rows-1)) and not((col+h+v)>(cols-1)):
                                    #print(f"    {row+v}.{col+h+v}")
                                    #print(f"    {matriz[row+v][col+h+v]}")
                                    if board[row+v][col+h+v] == player:
                                        cant+=1
                            #print("---")
                            if cant is n_line:
                                print(f"{n_line} en raya!")
                                return player
                #print("--")
            #print("-")
    return -1
def checkDiagonal2():
    for player in range(1,3):
        for col in range(1):
            for row in range(rows):
                if not(row + (n_line-1)>(rows-1)):
                    for h in range(0,n_line):
                        cant=0
                        #print("Comprobando##")
                        for v in range(0,n_line):
                            if not((cols-1-h-v) < 0):
                                #print(f"    {matriz[rows-1-v][cols-1-h-v]}")
                                #print(f"    {row+v}.{cols-1-h-v}")
                                if board[row+v][cols-1-h-v] == player:
                                    cant+=1
                        if cant is n_line:
                            print(f"{n_line} line!")
                            return player
                        #print("---")
                #print("--")
            #print("-")
    return -1
def nextPlayer(nPlayer):
    if nPlayer==1:
        return 2
    return 1

def totalTokens():
    fichaColumnas = [0,0,0,0,0]
    totalTokens= 0

    for i in range(0,rows):
        for j in range(0,cols):
            if board[i][j] != 0:
                fichaColumnas[j]+=1
                totalTokens+=1
    return totalTokens

def tokenQuantityInColumn(column):
    total=0
    for row in range(0,rows):
        if board[row][column-1] != 0:
            total+=1
    return total

def positionToPlace(column):
    print(f"quantity:{tokenQuantityInColumn(column)}")
    if holeInColumn(column):
        return ((rows-tokenQuantityInColumn(column)))

def holeInColumn(column):
    if tokenQuantityInColumn(column) != rows:#cuantas hay en vertical
        return True
    return False

#board=[[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24]]
def printBoardOnConsole():
    for i in range(rows):
        print(board[i])

def printVisualBoard():
    for i in range(1,rows+1):
        pygame.draw.line(window, color['WHITE'], (0,i*spaceY), (board_width,i*spaceY), width=3)
    for i in range(1,cols):
        pygame.draw.line(window, color['WHITE'], (i*spaceX,0), (i*spaceX,board_height), width=3)

    for row in range(1,rows+1):
        for col in range(1,cols+1):
            pygame.draw.circle(window,color['WHITE'],( spaceX*(col-1/2) , spaceY*(row-1/2) ),token_radius) 
    print_text("Turn of the player: ", (window_width/2-65,board_height+35),25)
    printPlayer(player, (window_width/2+110,board_height+35),40)
    
    for row in range(1,rows+1):
        for col in range(1,cols+1):
            if board[row-1][col-1] == 1:
                pygame.draw.circle(window,color['RED'],( spaceX*(col-1/2) , spaceY*(row-1/2) ),token_radius) # (col-1)*(spaceX/2) + col*(spaceX/2) = spaceX*(col-1/2)
            elif board[row-1][col-1]==2:
                pygame.draw.circle(window,color['CYAN'],( spaceX*(col-1/2) , spaceY*(row-1/2) ),token_radius)
    drawCloseButton()

button_closeRECT = pygame.Rect(window_width/2-int(120/2),window_height-50-int(40/2), 120, 40)
printBoardOnConsole()
player=1
printVisualBoard()

while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                print("click")
                posX=pos[0]
                for i in reversed(range(1,cols+1)):
                    if posX > (i-1) * board_width/cols and gameFinished is False:
                        print(f"Click en column numero {i} ")
                        if addStep(player,i) == True:
                            if not(isThereLine() == True):
                                player=nextPlayer(player)
                        break;
                if button_closeRECT.collidepoint(pos):
                    active=False
    posX,posY = pygame.mouse.get_pos()
    if button_closeRECT.collidepoint((posX,posY)):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    elif posX<=board_width and posY<=board_height and gameFinished is False: 
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    if gameFinished is False:
        clear()
        printVisualBoard()
    else:
        clear()
        printVisualBoard()
        pygame.draw.rect(window, color['WHITE'], rectangulo((window_width/2, (window_height+board_height)/2),window_width,window_height-board_height))
        print_text("The player won:", (window_width/2,window_height-160),35)
        printPlayer(player_won, (window_width/2,window_height-120),50)
        drawCloseButton()
    pygame.time.Clock().tick(30)
    pygame.display.update()