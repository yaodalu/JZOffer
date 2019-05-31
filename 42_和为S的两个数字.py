# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        start,end = 0,len(array)-1                                  
        while start <= end:
            if array[start] + array[end] < tsum:          #如果和小于tsum,那么右移start指针
                start += 1                                              
            elif array[start] + array[end] > tsum:        #如果和大于tsum,那么左移end指针
                end -= 1
            else:
                return [array[start],array[end]]          #当和等于tsum时，保证start距离end最远，即乘积最小
        return
    
if __name__ == "__main__":
    print Solution().FindNumbersWithSum([1,2,4,7,11,16],10)
