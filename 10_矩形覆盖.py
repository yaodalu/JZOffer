# -*- coding: utf-8 -*-
class Solution:
    def rectCover1(self,number):
        """递归版本"""
        if number == 0:
            return 0            
        if number == 1:                                                     #f(1)有一种形式
            return 1
        if number == 2:                                                     #f(2)有两种形式
            return 
        return self.rectCover1(number-2)+self.rectCover1(number-1)          #f(n)=f(n-1)+f(n-2)，从最后开始考虑

    def rectCover2(self,number):
        """非递归版本"""
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        a,b,res = 1,2,0
        for i in range(2,number):
            res = a+b
            a = b
            b = res
        return res
            
if __name__ == "__main__":
    solution = Solution()
    print solution.rectCover1(4)
