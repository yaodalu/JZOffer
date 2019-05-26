# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        pushL,popL = len(pushV),len(popV)
        if popL == 0:
            return false
        j,stack = 0,[]
        for i in range(pushL):
            stack.append(pushV[i])
            while j < popL and stack[-1] == popV[j]:            #无弹出操作的两种情况:1.popV[j]不在stack中 2.在stack中但不是栈顶
                stack.pop()
                j += 1
        return len(stack) == 0                              

if __name__ == "__main__":
    print Solution().IsPopOrder([1,2,3,4,5],[4,3,5,1,2])
        
