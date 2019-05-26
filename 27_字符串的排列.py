# -*- coding:utf-8 -*-
import collections

class Solution:
    def Swap(self,taskStr):
        resultList = []
        taskList = list(taskStr)
        for start in range(len(taskStr)-1):
            for end in range(1,len(taskStr)):
                taskList[start],taskList[end] = taskList[end],taskList[start]
                changeStr = ''.join(taskList)
                if  changeStr not in resSet:
                    resSet.add(changeStr)
                    resultList.append(changeStr)
        return resultList

    def Permutation(self, ss):
        """全排列版本"""
        goal = reduce(lambda x,y:x*y,range(1,len(ss)+1))
        q = collections.deque()
        q.appendleft(ss)
        global resSet
        resSet = set()
        resSet.add(ss)

        while len(resSet) != goal:
            taskStr = q.pop()
            resultList = self.Swap(taskStr)
            for result in resultList:
                q.appendleft(result)
        resList = []
        while resSet:
            resList.append(resSet.pop())
        resList.sort()
        print resList
    
if __name__ == "__main__":
    Solution().Permutation('a')

