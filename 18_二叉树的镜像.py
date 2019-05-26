# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
    def printNode(self,x):                                                                  #测试函数
        if x is None:
            return 
        queue = [x]
        while queue:
            node = queue.pop(0)
            print node.val,
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right) 

class Solution:
    def Mirror(self, root):
        if root is None:                                                                    #处理空节点
            return
        elif root.left is None and root.right is None:                                      #处理叶节点    
            return root
        else:
            root.left,root.right = self.Mirror(root.right),self.Mirror(root.left)           #递归交换左右子树
            return root

if __name__ == "__main__":
    tree1 = TreeNode(8)
    tree1.left = TreeNode(6)
    tree1.right = TreeNode(10)
    tree1.left.left = TreeNode(5)
    tree1.left.right = TreeNode(7)
    tree1.right.left = TreeNode(9)
    tree1.right.right = TreeNode(11)

    newTree = Solution().Mirror(tree1)
    print newTree.printNode(newTree)
