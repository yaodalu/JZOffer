# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        """递归中序+排序"""
        inOrderList = self.SerializeInOrder(pRoot)
        if k <= 0 or k > len(inOrderList):
            return None
        return inOrderList[k-1]
    
    def SerializeInOrder(self,root,inOrderList=[]):
        """中序递归版本"""
        if not root:
            return inOrderList
        self.SerializeInOrder(root.left,inOrderList)
        inOrderList.append(root.val)
        self.SerializeInOrder(root.right,inOrderList)
        return inOrderList

if __name__ == "__main__":
    tree = TreeNode(8)
    tree.left = TreeNode(6)
    tree.right = TreeNode(10)
    tree.left.left = TreeNode(5)
    tree.left.right = TreeNode(7)
    tree.right.left = TreeNode(9)
    tree.right.right = TreeNode(11)

    solution = Solution()
    print solution.SerializeInOrder(tree)
    print solution.KthNode(tree,7)
