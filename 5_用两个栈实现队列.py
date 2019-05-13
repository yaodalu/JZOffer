# -*- coding: utf-8 -*-
class Solution:
    def __init__(self):
        self.stack,self.temp = [],[]        
        
    def push(self,node):
        self.stack.append(node)

    def pop1(self):
        if self.stack is None:
            return
        while self.stack:
            self.temp.append(self.stack.pop())              #将栈内元素弹出到辅助栈，首元素是辅助栈的栈顶元素
        res = self.temp.pop()
        while self.temp:
            self.stack.append(self.temp.pop())              #将辅助栈内元素返回到栈中，恢复入栈顺序
        return res
    
    def pop2(self):                                            
        if not self.temp:                                     #如果缓冲区为零
            while self.stack:                                 #就将栈内元素全部弹出到缓冲区
                self.temp.append(self.stack.pop())              
        return self.temp.pop()      
    
if __name__ == "__main__":
    solution = Solution()
    for i in range(10):
        solution.push(i)
    for i in range(10):
        print solution.pop1(),
    
