import pygame, sys
from pygame.locals import *
import node

global M 
M = 3
#size of matrix
matrix = [ [ 0 for i in range(M) ] for j in range(M) ]

#block Size
BLOCKSIZE = 50
#x,o constant
XCONSTANT=1
OCONSTANT=2

WINDOWWIDTH  = M*BLOCKSIZE
WINDOWHEIGHT = M*BLOCKSIZE

FPS = 30

xImg = pygame.image.load('x_Img.png')
xImg = pygame.transform.scale(xImg,(BLOCKSIZE,BLOCKSIZE))

oImg = pygame.image.load('o_Img.png')
oImg = pygame.transform.scale(oImg,(BLOCKSIZE,BLOCKSIZE))

         # R G B
BLACK    = ( 0,  0  ,0)
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60, 60, 100)
WHITE    = (255, 255, 255)
RED      = (255, 0, 0)
GREEN    = ( 0, 255, 0)
BLUE     = ( 0, 0, 255)
YELLOW   = (255, 255, 0)
ORANGE   = (255, 128, 0)
PURPLE   = (255, 0, 255)
CYAN     = ( 0, 255, 255)


def main():
    pygame.init()
    
    global FPSCLOCK, DISPLAYSURF
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Tic Tac Toe Game')
    mousex = -1 # used to store x coordinate of mouse event
    mousey = -1 # used to store y coordinate of mouse event
    mouseClicked = False

    turn = OCONSTANT # Player go first
    
    while True: # main game loop
        DISPLAYSURF.fill(WHITE)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

        if turn == OCONSTANT and mouseClicked:
            column = int(mousex/BLOCKSIZE)
            row = int(mousey/BLOCKSIZE)  
            matrix[row][column] = OCONSTANT
            # update game state
            game = node.Node(OCONSTANT,(row,column),matrix)
            #swap turn
            if turn == OCONSTANT:
                turn = XCONSTANT
            else:
                turn = OCONSTANT
            mouseClicked = False

        elif turn == XCONSTANT and not mouseClicked:
            action = node.MiniMax_Decision(game)
            row = action[0]
            column = action[1]
            matrix[row][column] = XCONSTANT
            #update game state
            game = node.Node(XCONSTANT,(row,column),matrix)
            #swap turn
            if turn == OCONSTANT:
                turn = XCONSTANT
            else:
                turn = OCONSTANT
        #########################################################################################
        # draw x,o to screen
        draw()

        #draw lines
        for i in range(M):
            pygame.draw.line(DISPLAYSURF, BLACK, (0,i*BLOCKSIZE), (WINDOWHEIGHT, i*BLOCKSIZE))
            pygame.draw.line(DISPLAYSURF, BLACK, (i*BLOCKSIZE,0), (i*BLOCKSIZE, WINDOWWIDTH))
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        #########################################################################################        
        if mousex > 0 and mousey >0:
            if game.terminal():
                if game.ultility() == 1:
                    print("X wins")
                elif game.ultility() == -1:
                    print("O win")
                else:
                    print("draw")
                break
        


# assign proper value to matrix 
def setX(x,y):
    if x < 0 and y < 0:
        return
    column = int(x/BLOCKSIZE)
    row = int(y/BLOCKSIZE)
    if matrix[row][column]==0:
        matrix[row][column] = XCONSTANT
def setO(x,y):
    if x < 0 and y < 0:
        return
    column = int(x/BLOCKSIZE)
    row = int(y/BLOCKSIZE)
    if matrix[row][column]==0:
        matrix[row][column] = OCONSTANT

# draw matrix x,o 
def draw():
    for i in range(M):
        for j in range(M):
            if matrix[i][j]==XCONSTANT:
                DISPLAYSURF.blit(xImg, (j*BLOCKSIZE, i*BLOCKSIZE))
            if matrix[i][j]==OCONSTANT:
                DISPLAYSURF.blit(oImg, (j*BLOCKSIZE, i*BLOCKSIZE))




main()