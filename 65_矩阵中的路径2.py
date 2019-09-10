# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        if matrix is None or rows < 1 or cols < 1 or path is None:
            return False
        visited = [False]*(rows*cols)
        pathIndex = 0
        for row in range(rows):
            for col in range(cols):
                if self.hasPathCore(matrix,rows,cols,row,col,path,pathIndex,visited):
                    return True
        return False
                
    def hasPathCore(self,matrix,rows,cols,row,col,path,pathIndex,visited):
        if pathIndex == len(path):
            return True
        hasPath = False
        if row >= 0 and row < rows and col >= 0 and col <cols and matrix[row*cols+col] == path[pathIndex] and not (visited[row*cols+col]):
            pathIndex += 1
            visited[row*cols+col] = True
            hasPath = self.hasPathCore(matrix,rows,cols,row,col-1,path,pathIndex,visited) \
                     or self.hasPathCore(matrix,rows,cols,row-1,col,path,pathIndex,visited) \
                     or self.hasPathCore(matrix,rows,cols,row,col+1,path,pathIndex,visited) \
                     or self.hasPathCore(matrix,rows,cols,row+1,col,path,pathIndex,visited)
            if not hasPath:
                pathIndex -= 1
                visited[row*cols+col] = False
        return hasPath


if __name__ == "__main__":
    matrix = ['a','b','c','e','s','f','c','s','a','d','e','e']
    rows = 3
    cols = 4
    path = ['b','c','a']
    print Solution().hasPath(matrix,rows,cols,path)
