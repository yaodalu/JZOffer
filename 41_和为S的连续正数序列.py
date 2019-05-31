# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self,tsum):
        res = []
        i = tsum
        while i >= 2:
            if i%2 == 0 and divmod(tsum,i)[1] != 0 and divmod(float(tsum)/i*10,5)[1] == 0 and tsum/i-i/2+1 >= 1 :          #偶数个,那么中位数的小数部分必为0.5                                                             
                res.append([x for x in range(int(tsum/i)-i/2+1,int(tsum/i)+i/2+1)])
            if i%2 != 0 and tsum%i == 0 and tsum/i-(i-1)/2 >= 1:                                                           #奇数个,那么中位数必为整数  
                res.append([x for x in range(tsum/i-(i-1)/2,tsum/i+(i+1)/2)])
            i -= 1
        return res
                
if __name__ == "__main__":
    print Solution().FindContinuousSequence(9)
