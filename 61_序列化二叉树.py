# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def Serialize(self, root,preOrderList=[]):                          
        """前序递归版本"""
        if not root:
            preOrderList.append('$')
            return preOrderList
        preOrderList.append(root.val)
        self.Serialize(root.left,preOrderList)
        self.Serialize(root.right,preOrderList)
        return preOrderList

    def SerializeInOrder(self, root,inOrderList=[]):
        """中序递归版本"""
        if not root:
            inOrderList.append('$')
            return inOrderList
        self.SerializeInOrder(root.left,inOrderList)
        inOrderList.append(root.val)
        self.SerializeInOrder(root.right,inOrderList)
        return inOrderList
    
    def reConstructBinaryTree(self,pre,tin):
        # write code here
        if len(pre) == 0:                                                                               #没有子树
            return None
        elif len(pre) == 1:                                                                             #pre[0]对应叶节点
            return TreeNode(pre[0])
        else:
            root = TreeNode(pre[0])
            rootIndex = tin.index(pre[0])                                                   
            root.left = self.reConstructBinaryTree(pre[1:rootIndex+1],tin[:rootIndex+1])                #中序中，根节点左侧为左子树
            root.right = self.reConstructBinaryTree(pre[rootIndex+1:],tin[rootIndex+1:])                #中序中，根节点右侧为右子树 
            return root

if __name__ == "__main__":
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)
    tree1.left.left = TreeNode(4)
    tree1.right.left = TreeNode(5)
    tree1.right.right = TreeNode(6)

    solution = Solution()
    pre = solution.Serialize(tree1)
    tin = solution.SerializeInOrder(tree1)
    root = solution.Deserialize(pre,tin)


