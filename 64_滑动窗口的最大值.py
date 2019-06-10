# -*- coding:utf-8 -*-
from collections import deque

class Solution:
    def maxInWindows(self, num, size):                      #复杂度O(n)
        # write code here
        if size == 0:
            return []
        queue,res = deque(),[]
        for i in range(len(num)):
            while queue and i-size+1 > queue[0]:            #判断queue[0]是否在窗口中       
                queue.popleft() 
            while queue and num[queue[-1]]<num[i]:          #弹出queue中比num[i]小的数，使得queue中下标对应的值降序
                queue.pop()
            queue.append(i)
            if i >= size -1:
                res.append(num[queue[0]])
        return res
    
def getSlideWindowMax(num,size):
    """测试函数"""
    if size == 0:
        return []
    res = []
    for i in range(len(num)-size+1):                        #复杂度size*O(n)
        temp = num[i:i+size]
        res.append(max(temp))
    return res
        
if __name__ == "__main__":
    num = [2,3,4,2,6,2,5,1]
    size = 3
    solution = Solution()
    print solution.maxInWindows(num,size) == getSlideWindowMax(num,size)
