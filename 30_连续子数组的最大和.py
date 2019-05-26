# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):    
        if len(array)<=0:
            return []
        temp_sum = 0
        list_sum = []
        for i in array:
            temp_sum = temp_sum + i
            list_sum.append(temp_sum)           
            if temp_sum > 0:
                continue
            else:
                temp_sum = 0                        #当连续子数组的累加和小于零时,重新开始计算累加和
        return max(list_sum)

if __name__ == "__main__":
    print Solution().FindGreatestSumOfSubArray([6,-3,-2,7,-15,1,2,2])
