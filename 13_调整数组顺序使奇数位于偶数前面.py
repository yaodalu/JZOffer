# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray1(self, array):
        """快排版本"""                                                                   #快排不具备稳定性,复杂度O(n)
        array = [1] + array
        low,high,i = 0, len(array),1
        while i < high:
            if array[i]%2 != 0:                                                         #如果是奇数
                low -= 1
                i += 1
            else:                                                                       #如果是偶数
                high -= 1
                array[high],array[i] = array[i],array[high]
        return array[1:]

    def reOrderArray2(self,array):
        """函数式编程版本"""
        return filter(lambda x: x%2 != 0,array) + filter(lambda x: x%2 == 0,array)      

    def reOrderArray3(self,array):                      
        """插入版本"""                                                                  #插入排序具有稳定性,复杂度O(n^2)
        length = len(array)                 
        for i in range(1,length):
            for j in range(i,0,-1):                                                    
                if (array[j-1]%2 == 0) and (array[j]%2 != 0):                          #只有当前一个为偶,后一个为奇数时才交换
                    array[j],array[j-1] = array[j-1],array[j]
                else:
                    break
        return array
        
if __name__ == "__main__":
    array = [2,2,3,4,5,6,7,8]
    print Solution().reOrderArray3(array)
                
        
