# -*- coding:utf-8 -*-
##class Solution:
##    def GetNumberOfK(self, data, k):                          #复杂度O(n)
##        """Dict版本"""
##        temp = {}
##        for i in data:
##            temp[i] = temp.get(i,0)+1
##        return temp.get(k,0)
    
class Solution:
    def GetNumberOfK(self, data, k):                            #复杂度为O(logn)
        if not data or not k:
            return 0
        if data[-1] == data[0] == k:                            #特殊情况[1,1,1,1],data是list顺序表,查找是O(1)
            return len(data)
        frist = self.getFrist(data,k)
        last = self.getLast(data, k)
        if frist > -1 and last > -1:
            return last - frist + 1
        return 0

    def getFrist(self, data, k):
        """二分查找数组中k的第一位"""
        begin = 0
        end = len(data) - 1
        mid = int((begin + end)/2)
        while begin <= end:
            if data[mid] < k:
                begin = mid + 1
            elif data[mid] > k:
                if k == data[begin]:                            #当k在前半段时，判断首元素是否是k,如果是直接返回
                    return begin
                end = mid - 1
            else:
                if mid <= begin or data[mid-1] != k:            #mid-1是否等于k，不等于说明mid就是第一个等于k的下标，等于就要往前考虑
                    return mid
                else:                              
                    end = mid - 1
            mid = int((begin + end)/2)
        return -1

    def getLast(self, data, k):
        """二分查找数组中k的最后一位"""
        begin = 0
        end = len(data) - 1
        mid = int((begin + end)/2)
        while begin <= end:
            if data[mid] < k:
                if data[end] == k:                              #当k在后半段时，判断尾元素是否是k,如果是直接返回
                    return end
                begin = mid + 1
            elif data[mid] > k:
                end = mid - 1
            else:
                if mid >= end or data[mid+1] != k:
                    return mid
                else:
                    begin = mid + 1
            mid = int((begin + end)/2)
        return -1

if __name__ = "__main__":
    data = [1,3,3,3,3,4,5]
    k = 2
    Solution().GetNumberOfK(data,k)
    
