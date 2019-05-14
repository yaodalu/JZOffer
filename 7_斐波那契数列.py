# -*- coding: utf-8 -*-
class Solution:
    def Fibonacci(self,n):
        """递归版本"""
        if n == 0:                                               #时间复杂度?
            return 0
        if n == 1:
            return 1
        return self.Fibonacci(n-1)+self.Fibonacci(n-2)      

    def Fibonacci2(self,n):
        """迭代版本"""
        num1,num2,res = 0,1,n
        for i in range(n-1):
            res = num1 + num2
            num1 = num2
            num2 = res                       
        return res
    
    def Fibnacci3(self,n):
        """动态规划版本"""
        pass

##    def fibGenerator(self):
##        """生成器版本"""
##        num1,num2,res = 0,1,0
##        while True:
##            res = num1 + num2
##            yield res
##            num1 = num2
##            num2 = res

if __name__ == "__main__":
    solution = Solution()
    print solution.Fibonacci2(6) 
        
