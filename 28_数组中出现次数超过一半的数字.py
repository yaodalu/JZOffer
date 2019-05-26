# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution1(self, numbers):
        """set过滤重复值"""
        if len(numbers) == 0:
            return 0
        if len(numbers) == 1:
            return numbers[0]
        numberSet,length = set(numbers),len(numbers)
        while numberSet:
            number = numberSet.pop()
            if numbers.count(number) > length/2:                            #计算每个number的次数
                return number
        return 0
    
    def MoreThanHalfNum_Solution2(self, numbers):
        """阵地攻守版本"""
        if len(numbers) == 0:
            return 0
        if len(numbers) == 1:
            return numbers[0]
        i,count = 0,1
        for j in range(1,len(numbers)):                                     
            if numbers[j] == numbers[i]:                                    #如果相同,次数加1
                count += 1
            else:
                count -= 1
            if count == 0:                                                  #如果为0,说明前j个数字中number[i]没有超过一半,重新计数
                i,count = j,1                                               #退出循环时,number[i]有可能出现次数超过一半
        count = 0
        for j in range(len(numbers)):
            if numbers[j] == numbers[i]:
                count += 1
        if count > len(numbers)/2:
            return numbers[i]
        else:
            return 0
        
if __name__ == "__main__":
    print Solution().MoreThanHalfNum_Solution1([1,2,3,2,2,2,5,4,2])
        
        
