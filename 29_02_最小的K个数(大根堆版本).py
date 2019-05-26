# -*- coding: utf-8 -*-
from Queue import PriorityQueue
class Comparable():
    """比较器"""
    def __init__(self,val):
        self.val = val    
    def __cmp__(self,other):
        if self.val > other.val:
            return False
        else:
            return True


class MyPriQueue(PriorityQueue):                                #创建大根堆
    """含比较器的优先队列"""
    def __init__(self,comparableObj):
        PriorityQueue.__init__(self)
        self.comparableObj = comparableObj

    def add(self,val):                                     
        self.put(self.comparableObj(val))

    def poll(self):
        return self.get()

    def peek(self):
        val = self.get().val
        self.put(self.comparableObj(val))
        return val

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        minQ = MyPriQueue(Comparable)
        for i in range(k):                                      #构建个数为k的大根堆,复杂度k*log(k)
            minQ.add(tinput[i])
        for j in range(k,len(tinput)):
            if minQ.peek() > tinput[j]:                         #如果tinput[j]比堆顶大,说明最小的k个数中包含tinput[j],需要替换大根堆中的元素. (n-k)*logk. 
                minQ.poll()
                minQ.add(tinput[j])
        for i in range(k):
            print minQ.poll().val,                              #复杂度为O(nlogk)
            
if __name__ == "__main__":
    Solution().GetLeastNumbers_Solution([4,5,1,6,2,7,3,8],5)
