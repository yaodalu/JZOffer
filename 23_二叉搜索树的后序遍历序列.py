# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if len(sequence) == 0:
            return False
        return self.judge(sequence,0,len(sequence)-1)

    def judge(self,sequence,low,high):                                                    
        if low >= high:                                                              #对应三种情况:123(high,high-1),321(low,low-1),132(low,low)(high,high)                                     
            return True                                            
        i = high
        while (i>low) and sequence[i-1]>sequence[high]:                              #while循环从尾到头,确定左右子树分界线,循环次数不确定
            i -= 1                                                                   #退出循环时,i-1位于左子树序列部分最后一个
        for j in range(i-1,-1,-1):
            if sequence[j] > sequence[high]:
                return False
        return self.judge(sequence,low,i-1) and self.judge(sequence,i,high-1)        

if __name__ == "__main__":
    sequence = [1,3,2,5,7,6,4]
    print Solution().VerifySquenceOfBST(sequence)
    
      
            
                
