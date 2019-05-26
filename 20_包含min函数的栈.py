# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack,self.minStack = [],[]
        
    def push(self, node):
        if (not self.stack) or self.minStack[-1] >= node:
            self.stack.append(node)
            self.minStack.append(node)
        else:
            self.stack.append(node)
            self.minStack.append(self.minStack[-1])
            
    def pop(self):
        self.minStack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]
    
    def min(self):
        return self.minStack[-1]

if __name__ == "__main__":
    solution = Solution()
    nodeList = [3,2,55,4,1]
    for node in nodeList:
        solution.push(node)
    print solution.min()
    solution.pop()
    print solution.min()
    
