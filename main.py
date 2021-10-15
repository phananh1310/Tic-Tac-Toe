import pygame, sys
from pygame.locals import *
import Game
from setting import *

def main():
    pygame.init()
    
    global FPSCLOCK, DISPLAYSURF
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Tic Tac Toe Game')
    mousex = -1 # used to store x coordinate of mouse event
    mousey = -1 # used to store y coordinate of mouse event
    mouseClicked = False

    turn = O # Player go first
    
    while True: # main game loop
        DISPLAYSURF.fill(WHITE)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

        if turn == O and mouseClicked:
            column = int(mousex/BLOCKSIZE)
            row = int(mousey/BLOCKSIZE)  
            matrix[row][column] = O
            # update game state
            game = Game.Game(O,(row,column),matrix)
            #swap turn
            if turn == O:
                turn = X
            else:
                turn = O
            mouseClicked = False

        elif turn == X and not mouseClicked:
            action = Game.MiniMax_Decision(game)
            row = action[0]
            column = action[1]
            matrix[row][column] = X
            #update game state
            game = Game.Game(X,(row,column),matrix)
            #swap turn
            if turn == O:
                turn = X
            else:
                turn = O
        ###########################################
        # draw x,o to screen with line
        draw()
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        ############################################  
        # check terminal condition. Notify player at the console   
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
        matrix[row][column] = X
def setO(x,y):
    if x < 0 and y < 0:
        return
    column = int(x/BLOCKSIZE)
    row = int(y/BLOCKSIZE)
    if matrix[row][column]==0:
        matrix[row][column] = O

# draw matrix x,o 
def draw():
    for i in range(M):
        for j in range(M):
            if matrix[i][j]==X:
                DISPLAYSURF.blit(xImg, (j*BLOCKSIZE, i*BLOCKSIZE))
            if matrix[i][j]==O:
                DISPLAYSURF.blit(oImg, (j*BLOCKSIZE, i*BLOCKSIZE))

    #draw lines
    for i in range(M):
        pygame.draw.line(DISPLAYSURF, BLACK, (0,i*BLOCKSIZE), (WINDOWHEIGHT, i*BLOCKSIZE))
        pygame.draw.line(DISPLAYSURF, BLACK, (i*BLOCKSIZE,0), (i*BLOCKSIZE, WINDOWWIDTH))
   
##################################################################################################
main()