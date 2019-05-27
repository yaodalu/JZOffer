# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar1(self, s):
        """count函数法"""
        for i in range(len(s)):                
            if s.count(s[i]) == 1:
                return i
        else:
            return -1
        
    def FirstNotRepeatingChar2(self, s):
        """dict"""
        elemDict = {}
        for i in range(len(s)):                
            elemDict[s[i]] = elemDict.get(s[i],0)+1
        for i in range(len(s)):
            if elemDict[s[i]] == 1:
                return i
        else:
            return -1


if __name__ == "__main__":
    print Solution().FirstNotRepeatingChar2('bccvb')
            
