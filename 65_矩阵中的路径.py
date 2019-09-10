# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        matrixPos = self.buildMatrixPos(matrix,rows,cols)                           #创建矩阵
        global dirs
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]                                          #计算相邻位置
        initPos = []                                                                #创建初始位置,若存在，则弹出path首元素
        for i in range(rows):
            for j in range(cols):
                if matrixPos[i][j] == path[0]:
                    initPos.append((i,j))
        if len(initPos) == 0:         
            return False
        for pos in initPos:
            pathPos = path[:]
            if self.findPath(matrixPos,pos,pathPos):
                return True
            matrixPos = self.buildMatrixPos(matrix,rows,cols)
        return False


    def buildMatrixPos(self,matrix,rows,cols):                                   #创建矩阵
        matrixPos,k = [],0
        for i in range(rows):
            temp = []
            for j in range(cols):
                temp.append(matrix[k])
                k += 1
            matrixPos.append(temp)
        return matrixPos
    
    def findPath(self,matrixPos,pos,pathPos):
        self.mark(matrixPos,pos)
        if matrixPos[pos[0]][pos[1]] == pathPos[-1] and len(pathPos) == 1:
            return True
        pathPos.pop(0)
        for i in range(4):
            nextp = (pos[0]+dirs[i][0],pos[1]+dirs[i][1])
            if self.passable(matrixPos,nextp,pathPos):
                pathPos.pop(0)
                if self.findPath(matrixPos,nextp,pathPos):
                    return True
        return False
        
    def mark(self,matrixPos,pos):
        matrixPos[pos[0]][pos[1]] == 2                                              #在矩阵中位置pos处标2表示走过该位置

    def passable(self,matrixPos,pos,path):
        return matrixPos[pos[0]][pos[1]] == path[0]                                 #如果是path[-1]代表的字符，说明位置pos可行

if __name__ == "__main__":
    matrix = ['a','b','c','e','s','f','c','s','a','d','e','e']
    rows = 3
    cols = 4
    path = ['b','c']
    print Solution().hasPath(matrix,rows,cols,path)
    
