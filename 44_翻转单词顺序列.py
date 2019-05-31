# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        elemList = s.split(" ")
        return ' '.join(elemList[::-1])

if __name__ == "__main__":
    print Solution().ReverseSentence("")
