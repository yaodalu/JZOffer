# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        if not numbers:
            return False
        numList = [0,0,0,0,0,0,0,0,0,0,0]
        for num in numbers:
            numList[num%10] += 1
        zeroCount = numList[0]                            #大王小王的个数
        for i in range(1,12):                             #跳出循环时,i为第一个非大王小王的牌面
            if numList[i] == 2:
                return False
            if numList[i] == 1:
                break
        for j in range(i+1,i+6):                          #循环5次(多判断一次)是因为需要更新判断第五张牌后的zeroCount,如果为负数,说明2,3,4,5张牌均空
            if zeroCount >= 0:
                if numList[j] == 2:
                    return False
                if numList[j] == 0:
                    zeroCount -= 1
            else:
                return False
        return True
    
if __name__ == "__main__":
    print Solution().IsContinuous([11,3,0,0,5])
       
            
        
        
