# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
class Solution:
    def Print(self, pRoot):                                   
        evenList,oddList,res,layer = [pRoot],[],[],1
        while evenList or oddList:
            if layer%2 != 0:
                temp = []
                while evenList:
                    node = evenList.pop()                           #遍历偶数层顺序是先左后右，栈的先进后出
                    if node != None:
                        temp.append(node.val)
                        if node.left:                               #遍历偶数层时,先放入节点的左孩子,后放入节点的右孩子
                            oddList.append(node.left)
                        if node.right:
                            oddList.append(node.right)
                if temp:
                    res.append(temp)
                    layer += 1
            else:
                temp = []
                while oddList:
                    node = oddList.pop()                            #遍历奇数层顺序是先右后左                      
                    if node != None:
                        temp.append(node.val)
                        if node.right:                              #遍历偶数层时,先放入节点的右孩子,后放入节点的左孩子
                            evenList.append(node.right)
                        if node.left:
                            evenList.append(node.left)
                if temp:
                    res.append(temp)
                    layer += 1
        return res
                
if __name__ == "__main__":
    tree = TreeNode(5)
    tree.left = TreeNode(4)
    tree.left.left = TreeNode(3)
    tree.left.left.left = TreeNode(2)
    print Solution().Print(tree)
    
