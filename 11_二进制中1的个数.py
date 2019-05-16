# -*- coding: utf-8 -*-
class Solution:
    def NumberOf1_1(self,n):                            #假设n为int类型,32位. Python中的int是无限精度的
        if n >= 0:
            return bin(n).count('1')
        else:
            nStr = bin(n)[3:]
            temp = '1'*(32-len(nStr))
            transDict = {"1":'0','0':'1'}               #利用dict求反码
            for i in nStr:
                temp += transDict[i]                    #temp为反码
            return bin(int(temp,2)+1).count('1')        #反码+1=补码，再求二进制中1的个数

    def NumberOf1_2(self,n):
        return sum([(n>>i)&1 for i in range(0,32)])     #计算机中的负数用补码表示(正数的补码是本身).每次左移，判断末位是否为1

    def NumberOf1_3(self,n):    
        count = 0
        while (n != 0):                                 #循环次数是1的个数
            count += 1
            n = (n-1)&n                                 #每次使n的最低位的1为零(未必末位)
        return count
    
if __name__ == "__main__":
    solution = Solution()
    print solution.NumberOf1_3(-1)
