# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        total = 0
        for i in range(1,n+1):
            total += self.NumberOf1(i)
        return total

    def NumberOf1(self,number):
        """计算number中包含1的次数"""
        quotient,remainder = divmod(number,10)
        count = 0
        if quotient == 0:
            return 1 if remainder == 1 else 0
        while quotient != 0 or remainder != 0:                              #count记录余数为1出现的次数和,111=11*10+1=1*100+1*10+1
            if remainder == 1:
                count += 1
            quotient,remainder = divmod(quotient,10)
        return count

if __name__ == "__main__":
    print Solution().NumberOf1Between1AndN_Solution(13)
