# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        """sum函数法"""
        return sum(range(n+1))

    def Sum_Solution1(self,n):
        """位运算版本"""
        return n and n + self.Sum_Solution(n-1)    #当n=0时,返回0;当n=1时,返回1，此处考察位运算
        
if __name__ == "__main__":
    print Solution().Sum_Solution1(2)
