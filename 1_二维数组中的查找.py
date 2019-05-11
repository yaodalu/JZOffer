# -*- coding: utf-8 -*-
class Solution:
    def Find(self,target,array):
        row,col = 0,len(array[0])-1
        while (row <= len(array)-1) and (col >= 0):
            if target > array[row][col]:                        #目标值大,往下走
                row,col = row+1,col                   
            elif target < array[row][col]:                      #目标值小，往左走
                row,col = row,col-1
            else:
                return True
        return False

if __name__ == "__main__":
    solution = Solution()
    array = [[1,2,5,7],[3,4,9,13],[4,7,10,14],[5,8,11,15]]
    target = 18
    print solution.Find(target,array)
            
                
