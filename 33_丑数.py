# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index < 7:
            return index
        p2,p3,p5 = 0,0,0
        uglyList = [1]
        while len(uglyList) < index:
           ugly = min(uglyList[p2]*2,uglyList[p3]*3,uglyList[p5]*5)                 
           p2 = p2+1 if ugly == uglyList[p2]*2 else p2
           p3 = p3+1 if ugly == uglyList[p3]*3 else p3
           p5 = p5+1 if ugly == uglyList[p5]*5 else p5
           uglyList.append(ugly)
        return uglyList[-1]

if __name__ == "__main__":
    print Solution().GetUglyNumber_Solution(7)
     
