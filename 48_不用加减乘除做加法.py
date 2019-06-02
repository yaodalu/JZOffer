# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        """sum函数法版本"""
        return sum([num1,num2])

    def Add1(self,num1,num2):
        """位运算版本"""
        while num2 != 0:
            temp = (num1^num2)
            num2 = (num1&num2)<<1                   #num2记录进制位
            num1 = temp                             #num1记录位和
        return num1

if __name__ == "__main__":
    print Solution().Add1(8,7)
