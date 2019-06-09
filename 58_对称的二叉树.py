# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def isSymmetrical(self, pRoot):
        """递归镜像版本"""
        nodeList1,nodeList2 = [],[]
        inOrder = self.inOrderRecur(pRoot,nodeList1)
        symInOrder =  self.inOrderSymmetricRecur(pRoot,nodeList2)
        return inOrder == symInOrder
    
    def inOrderRecur(self,pRoot,nodeList=[]):
        """中序遍历列表"""
        if  not pRoot:
            nodeList += ['#']
            return nodeList
        nodeList += [pRoot.val]
        self.inOrderRecur(pRoot.left,nodeList)
        self.inOrderRecur(pRoot.right,nodeList)
        return nodeList

    def inOrderSymmetricRecur(self,pRoot,nodeList):
        """对称中序遍历列表"""
        if not pRoot:
            nodeList += ['#']
            return nodeList  
        nodeList += [pRoot.val]
        self.inOrderSymmetricRecur(pRoot.right,nodeList)
        self.inOrderSymmetricRecur(pRoot.left,nodeList)
        return nodeList

if __name__ == "__main__":
    tree = TreeNode(8)
    tree.left = TreeNode(6)
    tree.right = TreeNode(6)
    tree.left.left = TreeNode(5)
    tree.left.right = TreeNode(7)
    tree.right.left = TreeNode(7)
    tree.right.right = TreeNode(5)
    nodeList = []
    print Solution().inOrderRecur(tree,nodeList)
