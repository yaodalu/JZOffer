# -*- coding: cp936 -*-
class Solution:
    def minNumberInRotateArray(self,rotateArray):           #顺序遍历复杂度为O(n)
        if not rotateArray:
            return 0
        for i in range(len(rotateArray)-1):
            if rotateArray[i] > rotateArray[i+1]:           #出现降序
                return rotateArray[i+1]
        return rotateArray[0]                               #特殊情况，数组等值或者单元素数组

if __name__ == "__main__":
    rotateArray1 = [3,4,5,1,2]
    rotateArray2 = [2,2,2,2,2]
    rotateArray3 = [3]
    solution = Solution()
    print solution.minNumberInRotateArray(rotateArray1)
    print solution.minNumberInRotateArray(rotateArray2)
    print solution.minNumberInRotateArray(rotateArray3)
   
