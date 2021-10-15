import pygame

#########################
# score 
WIN = 100 # positive inf
LOSE = -WIN # negative inf

########################
global M # matrix size
M = 3 

SEQ = 3 # number of sequential X/O to win 

#size of matrix
matrix = [ [ 0 for i in range(M) ] for j in range(M) ]

#block Size
BLOCKSIZE = 50
#x,o constant
X=1
O=2

WINDOWWIDTH  = M*BLOCKSIZE
WINDOWHEIGHT = M*BLOCKSIZE

FPS = 30
# loading X,O image
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
