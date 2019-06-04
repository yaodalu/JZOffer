# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        numDict = {}
        for num in numbers:
            if numDict.get(num,0) == 1:
                duplication.append(num)
                return True
            numDict[num] = 1
        return False

if __name__ == "__main__":
    duplication = []
    print Solution().duplicate([2,1,3,1,4],duplication)
    print duplication
