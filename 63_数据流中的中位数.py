# -*- coding:utf-8 -*-
import random
from Queue import PriorityQueue

class MinRootComparable():
    """小根堆比较器"""
    def __init__(self,val):
        self.val = val    
    def __cmp__(self,other):
        if self.val < other.val:
            return False
        else:
            return True

class MaxRootComparable():
    """大根堆比较器"""
    def __init__(self,val):
        self.val = val    
    def __cmp__(self,other):
        if self.val > other.val:
            return False
        else:
            return True

class MyPriQueue(PriorityQueue):                                
    """含比较器的优先队列"""
    def __init__(self,comparableObj):
        PriorityQueue.__init__(self)
        self.comparableObj = comparableObj
        self.count = 0
    def add(self,val):                                     
        self.put(self.comparableObj(val))
        self.count += 1
    def poll(self):
        if self.count == 0:
            return
        self.count -= 1
        return self.get().val
    def peek(self):                                                                                     #如果为空，堆顶为None
        if self.count == 0:
            return
        val = self.get().val
        self.put(self.comparableObj(val))
        return val
    def getCount(self):
        return self.count
    
class Solution:
    """数据流中的中位数"""
    def __init__(self):
        self.minQ = MyPriQueue(MinRootComparable)                                                       #小根堆存储大数
        self.maxQ = MyPriQueue(MaxRootComparable)                                                       #大根堆存储小数
    def Insert(self, num):
        if self.maxQ.getCount() == 0:
            self.maxQ.add(num)
            return
        if self.maxQ.peek() > num:
            self.maxQ.add(num)
        else:
            if self.minQ.getCount() == 0:
                self.minQ.add(num)
                return
            if self.minQ.peek() > num:
                self.maxQ.add(num)
            else:
                self.minQ.add(num)
        self.modifySize()
    def modifySize(self):
        """调整堆的大小"""
        if self.minQ.getCount() == self.maxQ.getCount() + 2:
            self.maxQ.add(self.minQ.poll())
        if self.maxQ.getCount() == self.minQ.getCount() + 2:
            self.minQ.add(self.maxQ.poll())
    def GetMedian(self):
        if self.minQ.getCount() + self.maxQ.getCount() == 0:
            return 0
        minPeek,maxPeek = self.minQ.peek(),self.maxQ.peek()
        if (self.minQ.getCount() + self.maxQ.getCount()) % 2 != 0:
            return minPeek if self.minQ.getCount() > self.maxQ.getCount() else maxPeek
        else:
            return (minPeek + maxPeek) / 2.0

def getMedianForTest(numList):
    """测试函数"""
    copyList = numList[:]
    if not copyList:
        return 0
    if len(copyList)==1:
        return copyList[0]
    length = len(copyList)
    copyList.sort()
    if length % 2 != 0:
        return copyList[length/2]
    else:
        return (copyList[length/2]+copyList[length/2-1])/2.0

if __name__ == "__main__":     
    solution = Solution()
    numCount = 100
    numList = []
    for i in range(numCount):
        num = random.randint(1,100)
        numList.append(num)
        solution.Insert(num)
    print getMedianForTest(numList)
    print solution.GetMedian()
