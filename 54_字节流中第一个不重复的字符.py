# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def FirstAppearingOnce(self):                   #时间复杂度O(n),空间复杂度O(n)
        # write code here
        if not self.charList:
            return '#'
        return self.charList[0]
        
    def Insert(self, char):
        # write code here
        if  not self.charList:
            self.charList.append(char)
        elif char in self.charList:
            self.charList.remove(char)
        else:
            self.charList.append(char)
        
    def __init__(self):
        self.charList = []

if __name__ == "__main__":
    charStr = 'google'
    solution = Solution()
    for char in charStr:
        solution.Insert(char)
        print solution.FirstAppearingOnce(),
    
