# -*- coding: utf-8 -*-
class Solution:
    def printMatrix(self,matrix):
        startR,startC,endR,endC = 0,0,len(matrix)-1,len(matrix[0])-1
        while endR >= startR and endC >= startC:                            #矩阵的四个顶点由startR,startC,endR,endC唯一确定
            self.printEdge(matrix,startR,startC,endR,endC)
            endR,endC = endR-1,endC-1
            startR,startC = startR+1,startC+1
            
    def printEdge(self,matrix,startR,startC,endR,endC):
        if startR == endR:                                                  
            for i in range(startC,endC+1):
                print matrix[startR][i]
        elif startC == endC:
            for i in range(startR,endR+1):
                print matrix[i][startC]
        else:
            curR,curC = startR,startC
            while curC != endC:
                print matrix[curR][curC],
                curC += 1
            while curR != endR:
                print matrix[curR][curC],
                curR += 1
            while curC != startC:
                print matrix[curR][curC],
                curC -= 1
            while curR != startR:
                print matrix[curR][curC],
                curR -= 1
            
if __name__ == "__main__":
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    matrix = [[1]]
    Solution().printMatrix(matrix)
