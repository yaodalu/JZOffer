# -*- coding: utf-8 -*-
class Solution:
    def replaceSpace1(self,s):
        return s.replace(" ","%20")         #直接调用str的replace方法
    
    def replaceSpace2(self,s):
        sList = list(s)                     #转换成list,list可变,str不可变
        for i in range(len(sList)):
            if sList[i] == " ":
                 sList[i] = "%20"           #替换
        return "".join(sList)        

if __name__ == "__main__":
    s = "we are happy"
    solution = Solution()
    print solution.replaceSpace2(s)
    
