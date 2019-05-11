# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
    def preOrderRec(self,x):                                                                    #测试函数
        if x is None:
            return
        print x.val,
        self.preOrderRec(x.left)
        self.preOrderRec(x.right)
        
class Solution:
    def reConstructBinaryTree(self,pre,tin):                                                    #递归实现二叉树重建
        if len(pre) == 0:                                                                       #没有子树
            return None
        elif len(pre) == 1:                                                                     #pre[0]对应叶节点
            return TreeNode(pre[0])
        else:
            root = TreeNode(pre[0])
            rootIndex = tin.index(pre[0])                                                   
            root.left = self.reConstructBinaryTree(pre[1:rootIndex+1],tin[:rootIndex+1])       #中序中，根节点左侧为左子树
            root.right = self.reConstructBinaryTree(pre[rootIndex+1:],tin[rootIndex+1:])       #中序中，根节点右侧为右子树 
            return root

if __name__ == "__main__":
    pre = [1,2,4,7,3,5,6,8]
    tin = [4,7,2,1,5,3,8,6]
    solution = Solution()
    root = solution.reConstructBinaryTree(pre,tin)
    root.preOrderRec(root)
