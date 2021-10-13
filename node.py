from copy import deepcopy
M=3
XCONSTANT=1
OCONSTANT=2
class Node:
    def __init__(self, turn, position, matrix ):
        self.turn = turn
        self.matrix = deepcopy(matrix)
        self.position = position
        self.value = []

        self.matrix[position[0]][position[1]] = turn

    # store returned value when using minimax
    def appendValue(self, value):
        self.value.append(value)

    # return which player to move in this state
    def player(self):
        return self.turn
    
    # return list of legal move in this state
    def action(self):
        actions = []

        for i in range (M):
            for j in range (M):
                if self.matrix[i][j] == 0:
                    actions.append((i,j))
               
        return actions
    
    # check if state is a terminal state
    def terminal(self):
        # check if 3 in a row/ column/ diagonal
        if self.ultility() == 1 or self.ultility() == -1:
            return True

        # check full board
        for i in range(M):
            for j in range(M):
                if self.matrix[i][j]==0:
                    return False

        # else it's a draw
        return True 
    
    # return node after action(tuple of position) a taken on this state  
    def result(self , a):
        if self.player() == XCONSTANT:
            node=Node(OCONSTANT,a,self.matrix)
        else:
            node=Node(XCONSTANT,a,self.matrix)
        return node

    # ultility for terminal state 
    def ultility(self):
        if self.player() == XCONSTANT:
            score = 1
        else:
            score = -1

        if self.checkRow() or self.checkColumn() or self.checkDiagonal():
            return score
        # draw

                
        return 0
    
    # check at this position, is it 3
    def checkRow(self):
        list = []
        list.append(self.matrix[self.position[0]][self.position[1]])
        
        # list extend left and right
        i=0
        while self.position[1] - i > 0:
            i+=1
            list = [self.matrix[self.position[0]][self.position[1] - i]] + list
            if i==3-1:
                break
        
        i=0        
        while self.position[1]+i < M-1:
            i+=1   
            list.append(self.matrix[self.position[0]][self.position[1] + i])
            if i==3-1:
                break
            
        # we have the list with max length 2*M-1
        # check if there is a 3 coninuous equals in the list
        for j in range(len(list)-3+1):
            if list[j] == list[1+j] == list[j+2]!=0:
                return True
        return False

    def checkColumn(self):
        list = []
        list.append(self.matrix[self.position[0]][self.position[1]])
        
        # list extend left and right
        i=0
        while self.position[0] - i > 0:
            i+=1
            list = [self.matrix[self.position[0]-i][self.position[1]]] + list
            if i==3-1:
                break
        
        i=0        
        while self.position[0]+i < M-1:
            i+=1   
            list.append(self.matrix[self.position[0]+i][self.position[1]])
            if i==3-1:
                break
            
        # we have the list with max length 2*M-1
        # check if there is a 3 coninuous equals in the list
        for j in range(len(list)-3+1):
            if list[j] == list[1+j] == list[j+2]!=0:
                return True
        return False

    def checkDiagonal(self):
        # check two diagonal
        # first one - up left and down right
        list = []
        list.append(self.matrix[self.position[0]][self.position[1]])
        
        # list extend up left direction
        i=0
        while self.position[0] - i > 0 and  self.position[1]-i > 0:
            i+=1
            list = [self.matrix[self.position[0]-i][self.position[1]-i]] + list
            if i==3-1:
                break
        # list extend down right direction
        i=0        
        while self.position[0]+i < M-1 and self.position[1]+i < M-1:
            i+=1   
            list.append(self.matrix[self.position[0]+i][self.position[1]+i])
            if i==3-1:
                break
            
        # we have the list with max length 2*M-1
        # check if there is a 3 coninuous equals in the list
        for j in range(len(list)-3+1):
            if list[j] == list[1+j] == list[j+2]!=0:
                return True
        ###########################################################
        # Second diagonal - up right and down left       
        list = []
        list.append(self.matrix[self.position[0]][self.position[1]])
        # list extend up right direction
        i=0
        while self.position[0] - i > 0 and  self.position[1] + i < M-1:
            i+=1
            list = [self.matrix[self.position[0]-i][self.position[1]+i]] + list
            if i==3-1:
                break
        # list extend down left direction
        i=0        
        while self.position[0]+i < M-1 and self.position[1]-i > 0:
            i+=1   
            list.append(self.matrix[self.position[0]+i][self.position[1]-i])
            if i==3-1:
                break
            
        # we have the list with max length 2*M-1
        # check if there is a 3 coninuous equals in the list
        for j in range(len(list)-3+1):
            if list[j] == list[1+j] == list[j+2]!=0:
                return True
        return False

def MinValue(node):
    if node.terminal():
        return node.ultility()
    v = 2 # max infinity
    for nodeAction in node.action():
        v = min(v,MaxValue(node.result(nodeAction)))
    return v

def MaxValue(node):
    if node.terminal():
        return node.ultility()
    v = -2 # min infinity
    for nodeAction in node.action():
        v = max(v,MinValue(node.result(nodeAction)))
        node.appendValue(v)
    return v

def MiniMax_Decision(node):
    v = MaxValue(node)
    i=0
    for nodeAction in node.action():
        if v == node.value[i]:
            return nodeAction
        i+=1

#def test():
 #   matrix = [[1,2,2],[1,2,1],[0,0,0]]
 #   n = Node(XCONSTANT,(2,2),matrix)
  #  print(n.matrix)
  #  MaxValue(n)
   # print(n.value)


