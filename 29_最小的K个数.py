# -*- coding:utf-8 -*-
from Queue import PriorityQueue
class Comparable():
    """比较器"""
    def __init__(self,val):
        self.val = val    
    def __cmp__(self,other):
        if self.val < other.val:
            return -1
        else:
            return 1
        
class MyPriQueue(PriorityQueue):                                #创建小根堆
    """含比较器的优先队列"""
    def __init__(self,comparableObj):
        PriorityQueue.__init__(self)
        self.comparableObj = comparableObj

    def add(self,val):                                     
        self.put(self.comparableObj(val))

    def poll(self):
        return self.get()

    def peek(self):
        val = self.get()
        self.put(self.comparableObj(val))
        return val
    
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        minQ = MyPriQueue(Comparable)
        for i in range(len(tinput)):                            
            minQ.add(tinput[i])                                 #插入复杂度为n*O(logn)
        for j in range(k):
            print minQ.poll().val,                              #弹出复杂度为k*O(logn)

if __name__ == "__main__":
    Solution().GetLeastNumbers_Solution([4,5,1,6,2,7,3,8],5)
