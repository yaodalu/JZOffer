# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self,threshold, rows, cols):
        if threshold < 0 or rows <= 0 or cols <= 0:
            return 0
        visited = [False]*(rows*cols)
        count = self.movingCountCore(threshold,rows,cols,0,0,visited)
        return count
    
    def movingCountCore(self,threshold,rows,cols,col,row,visited):
        count = 0
        if self.check(threshold,rows,cols,row,col,visited):
            visited[row*cols+col] = True
            count = 1 + self.movingCountCore(threshold,rows,cols,row-1,col,visited) + \
                     self.movingCountCore(threshold,rows,cols,row,col-1,visited) + \
                     self.movingCountCore(threshold,rows,cols,row+1,col,visited) + \
                     self.movingCountCore(threshold,rows,cols,row,col+1,visited)
        return count
    
    def check(self,threshold,rows,cols,row,col,visited):
        """判断机器人能否进入坐标(row,col)的方格"""
        if row >= 0 and row < rows and col >= 0 and col < cols \
            and not visited[row*cols+col] and self.getDigitSum(row)+self.getDigitSum(col) <= threshold:
            return True
        return False

    def getDigitSum(self,number):
        """得到坐标的位数之和"""
        total = 0
        while number > 0:
            total += number % 10
            number /= 10
        return total

if __name__ == "__main__":
    print Solution().movingCount(10,1,100)
