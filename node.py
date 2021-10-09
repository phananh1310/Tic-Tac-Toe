M=8
XCONSTANT=1
OCONSTANT=2
class Node:
    def __init__(self, turn, position, matrix ):
        self.turn = turn
        self.matrix = matrix
        self.position = position
    
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
        #check row and column
        for i in range(3):
            if self.matrix[i][0]==self.matrix[i][1]==self.matrix[i][2]!=0:
                return True
            
            if self.matrix[0][i]==self.matrix[1][i]==self.matrix[2][i]!=0:
                return True
        
        #check diagonal
        if self.matrix[0][0]==self.matrix[1][1]==self.matrix[2][2]!=0:
            return True
        if self.matrix[0][0]==self.matrix[1][1]==self.matrix[2][2]!=0:
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
            self.matrix[a[0]][a[1]] = OCONSTANT
            node=Node(OCONSTANT,(a[0],a[1]),self.matrix)
        else:
            self.matrix[a[0]][a[1]] = OCONSTANT
            node=Node(XCONSTANT,(a[0],a[1]),self.matrix)
        self.matrix[a[0]][a[1]]=0
        return node

    # ultility for terminal state 
    def ultility(self):
        if self.player() == XCONSTANT:
            score =  1
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

        

        