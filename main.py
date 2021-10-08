import pygame, sys
from pygame.locals import *

M = 3
#size of matrix
matrix = [ [ 0 for i in range(M) ] for j in range(M) ]
#block Size
BLOCKSIZE = 100
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
    
    while True: # main game loop
        DISPLAYSURF.fill(WHITE)
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
        drawO(mousex,mousey)
            
        pygame.display.update()
        FPSCLOCK.tick(FPS)

# draw x,o and assign proper value to matrix 
def drawX(x,y):
    if x < 0 and y < 0:
        return
    row = int(x/BLOCKSIZE)
    column = int(y/BLOCKSIZE)
    if matrix[row][column]==0:
        matrix[row][column] = XCONSTANT
    for i in range(M):
        for j in range(M):
            if matrix[i][j]==XCONSTANT:
                DISPLAYSURF.blit(xImg, (i*BLOCKSIZE, j*BLOCKSIZE))

def drawO(x,y):
    if x < 0 and y < 0:
        return
    row = int(x/BLOCKSIZE)
    column = int(y/BLOCKSIZE)
    if matrix[row][column]==0:
        matrix[row][column] = OCONSTANT
    for i in range(M):
        for j in range(M):
            if matrix[i][j]==OCONSTANT:
                DISPLAYSURF.blit(oImg, (i*BLOCKSIZE, j*BLOCKSIZE))

main()