from copy import deepcopy
from setting import * 
import math

POSITIVE_INF = math.inf
NEGATIVE_INF = -math.inf
# FUNCTION 
##################################
# MINIMAX algorithm using 
# Alpha Beta pruning (a,b)
def MinValue(node,a,b):
    if node.terminal():
        return node.ultility()
    v = POSITIVE_INF # max infinity
    for nodeAction in node.action():
        v = min(v,MaxValue(node.result(nodeAction),a,b))
        if v <= a:
            return v
        b = min(b,v)
    return v

def MaxValue(node,a,b):
    if node.terminal():
        return node.ultility()
    v = NEGATIVE_INF # min infinity
    for nodeAction in node.action():
        v = max(v,MinValue(node.result(nodeAction),a,b))
        if v>=b:
            node.appendValue(v)
            return v
        a = max(a,v)
        node.appendValue(v)
    return v

def MiniMax_Decision(node):
    v = MaxValue(node,NEGATIVE_INF,POSITIVE_INF)
    i=0
    for nodeAction in node.action():
        if v == node.value[i]:
            return nodeAction
        i+=1
########################
# check is there is SEQ sequential in the list
def checkList(list,SEQ):
    count = 1
    i=0
    while i < len(list) - 1:
        if list[i+1] == list[i] != 0:
            count += 1
            if count == SEQ:
                return True
        else:
            count = 1 
        i+=1
    return False

################################
class Game:
    def __init__(self, turn, position, matrix):
        # Who and Where just go ?
        self.turn = turn
        self.position = position
        # a copy of matrix/ if not, it would affect outer matrix
        self.matrix = deepcopy(matrix)
        
        # list of ultility score in each legal actions
        self.value = []
        # update the state
        self.matrix[position[0]][position[1]] = turn

        # draw or not
        self.draw = False

    # method store returned value when using minimax
    def appendValue(self, value):
        self.value.append(value)

    # return which player to move in this state
    def player(self):
        return self.turn
    
    # return list of legal move in this state
    def action(self):
        actions = []

        for i in range(M):
            for j in range(M):
                if self.matrix[i][j]==0:
                    actions.append((i,j))
               
        return actions

    # check if state is a terminal state
    def terminal(self):
        # a list of row/ column/ diagonal in the current position with max length = 2 * SEQ - 1
        list = self.checkRow()
        if checkList(list,SEQ):
            return True
        
        list = self.checkColumn()
        if checkList(list,SEQ):
            return True 
        
        list = self.checkDiagonal1()
        if checkList(list,SEQ):
            return True

        list = self.checkDiagonal2()
        if checkList(list,SEQ):
            return True

        # check full board
        for i in range(M):
            for j in range(M):
                if self.matrix[i][j]==0:
                    return False

        # else it's a draw
        self.draw = True
        return True 

    # return node after action(tuple of position) a taken on this state  
    def result(self , a):
        if self.player() == X:
            game = Game(O,a,self.matrix)
        else:
            game = Game(X,a,self.matrix)
        return game

    # ultility for terminal state 
    def ultility(self):
        if self.draw:
            return 0
        
        if self.player() == X and self.terminal: 
            return WIN
        else:
            return LOSE   
    
    # Return a list based on current positon in a row/ column/ diagonal
    def checkRow(self):
        list = []
        list.append(self.matrix[self.position[0]][self.position[1]])
        
        # list extend left and right
        i=0
        while self.position[1] - i > 0:
            i+=1
            list = [self.matrix[self.position[0]][self.position[1] - i]] + list
            if i==SEQ-1:
                break
        
        i=0        
        while self.position[1]+i < M-1:
            i+=1   
            list.append(self.matrix[self.position[0]][self.position[1] + i])
            if i==SEQ-1:
                break
            
        # we have the list with max length 2*M-1
        return list       

    def checkColumn(self):
        list = []
        list.append(self.matrix[self.position[0]][self.position[1]])
        
        # list extend left and right
        i=0
        while self.position[0] - i > 0:
            i+=1
            list = [self.matrix[self.position[0]-i][self.position[1]]] + list
            if i==SEQ-1:
                break
        
        i=0        
        while self.position[0]+i < M-1:
            i+=1   
            list.append(self.matrix[self.position[0]+i][self.position[1]])
            if i==SEQ-1:
                break
            
        # we have the list with max length 2*M-1
        return list
    # first one - up left and down right
    def checkDiagonal1(self):
        list = []
        list.append(self.matrix[self.position[0]][self.position[1]])
        
        # list extend up left direction
        i=0
        while self.position[0] - i > 0 and  self.position[1]-i > 0:
            i+=1
            list = [self.matrix[self.position[0]-i][self.position[1]-i]] + list
            if i==SEQ-1:
                break
        # list extend down right direction
        i=0        
        while self.position[0]+i < M-1 and self.position[1]+i < M-1:
            i+=1   
            list.append(self.matrix[self.position[0]+i][self.position[1]+i])
            if i==SEQ-1:
                break
            
        # we have the list with max length 2*M-1
        return list
    
    # Second diagonal - up right and down left   
    def checkDiagonal2(self):
        list = []
        list.append(self.matrix[self.position[0]][self.position[1]])
        # list extend up right direction
        i=0
        while self.position[0] - i > 0 and  self.position[1] + i < M-1:
            i+=1
            list = [self.matrix[self.position[0]-i][self.position[1]+i]] + list
            if i==SEQ-1:
                break
        # list extend down left direction
        i=0        
        while self.position[0]+i < M-1 and self.position[1]-i > 0:
            i+=1   
            list.append(self.matrix[self.position[0]+i][self.position[1]-i])
            if i==SEQ-1:
                break
            
        # we have the list with max length 2*M-1
        return list

#########################
# TEST FUNCTION / CLASS
def test():
    matrix =[[1,1,2,1],
             [1,2,1,2],
             [1,0,2,1],
             [1,2,0,0]
            ]
    # game start with X in (0,0)
    game = Game(O,(2,2),matrix)

    print(game.ultility())
#test()

##########################