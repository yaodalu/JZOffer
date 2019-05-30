# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        temp = {}
        for i in array:
            temp[i] = temp.get(i,0)+1
        temp = filter(lambda x:x[1]==1,temp.items())
        return [x for x,_ in temp]


if __name__ == "__main__":
    array = [2,4,3,6,3,2,5,5]
    print Solution().FindNumsAppearOnce(array)
