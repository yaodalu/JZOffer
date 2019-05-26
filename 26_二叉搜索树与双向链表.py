# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Convert(self, pRootOfTree):
        """递归版本"""
        if not pRootOfTree:
            return
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        
        self.Convert(pRootOfTree.left)                                          #链接左子树
        left = pRootOfTree.left                                             
        if left:
            while left.right:
                left = left.right
            pRootOfTree.left,left.right = left,pRootOfTree                      #链接根节点和左子树中最右节点的双向链接
            
        self.Convert(pRootOfTree.right)                                         #链接右子树
        right = pRootOfTree.right
        if right:
            while right.left:
                right = right.left
            pRootOfTree.right,right.left = right,pRootOfTree                    #链接根节点和右子树中最左节点的双向链接

        while(pRootOfTree.left):
            pRootOfTree = pRootOfTree.left                                      #退出循环时,pRootOfTree指向二叉树中的最左节点
        return pRootOfTree
        
if __name__ == "__main__":
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.right = TreeNode(6)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(3)
    tree.right.left = TreeNode(5)
    tree.right.right = TreeNode(7)
    doubleList = Solution().Convert(tree)
    while doubleList.right != None:
        print doubleList.val,
        doubleList = doubleList.right
    print doubleList.val,
    print '\n'
    while doubleList != None:
        print doubleList.val,
        doubleList = doubleList.left 
    
