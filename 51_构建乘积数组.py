# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):                      #复杂度O(n^2)
        B = [1]*len(A)
        for i in range(len(B)):
            for j in range(len(A)):
                if j == i:
                    continue
                else:
                    B[i] *= A[j]
        return B

    def multiply1(self,A):                      #复杂度O(n)
        temp,B = 1,[]
        for i in range(len(A)):
            temp *= A[i]
        for i in range(len(A)):
            B.append(temp/A[i])
        return B

    
if __name__ == "__main__":
    A = [1,2,3,4]
    print Solution().multiply1(A)
