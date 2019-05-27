# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        return self.mergeSort(data,0,len(data)-1) % 1000000007
    
    def mergeSort(self,data,low,high):                                                                              
        if low == high:
            return 0                                                                                                #单元素数组的逆序对个数为0
        mid = (low+high)//2
        return self.mergeSort(data,low,mid) + self.mergeSort(data,mid+1,high) + self.merge(data,low,mid,high)       #逆序对总数p = [low,mid]和[mid+1,high]归并结果+之前若干次归并之和
    
    def merge(self,data,low,mid,high):                                                                  
        p1,p2 = low,mid+1                                                                                           #p1是[low,mid]的下标索引,p2是[mid+1,high]的下标索引
        temp,res = [],0
        while p1 <= mid and p2 <= high:
            if data[p1] <= data[p2]:
                temp.append(data[p1])
                p1 += 1
            else:
                temp.append(data[p2])
                res += mid - p1 + 1                                                                                 #计算逆序对
                p2 += 1
        while p1 <= mid:
            temp.append(data[p1])
            p1 += 1
        while p2 <= high:
            temp.append(data[p2])
            p2 += 1
        for i in range(len(temp)):                                                                                  #更新原数组
            data[low+i] = temp[i]
        return res                                                                                                  #返回本次归并产生的逆序对

if __name__ == "__main__":
    print Solution().InversePairs([1,2,3,4,5,6,7,0])
    
