# -*- coding: utf-8 -*-
class Solution:
    def jumpFloor(self,number):
        if number == 1:                     #一级台阶有1种跳法
            return 1
        if number == 2:                     #两级台阶有2种跳法
            return 2
        res,a,b = 0,1,2
        for i in range(2,number):
            res = a+b                       #f(n)=f(n-1)+f(n-2)
            a = b
            b = res
        return res

if __name__ == "__main__":
    solution = Solution()
    print solution.jumpFloor(4)
            
