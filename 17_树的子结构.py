# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
    def printNode(self,x):                                                                                                      #测试函数
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
    def HasSubtree(self, pRoot1, pRoot2):
        """判断pRoot2是不是pRoot1的子树"""
        if not pRoot1 or not pRoot2:
            return False
        return self.is_subtree(pRoot1,pRoot2) or self.HasSubtree(pRoot1.left,pRoot2) or self.HasSubtree(pRoot1.right,pRoot2)    #三种可能性：pRoot2是pRoot1的子树，pRoot2是pRoot1.left的子树，pRoot2是pRoot1.right的子树

    def is_subtree(self,A,B):
        """判断B子树是不是与A子树结构相同"""
        if not B:                                                                                                               #空树不是子树
            return True
        if not A or A.val != B.val:                                                                                             #(A树为空，B不空)|(A树不空，值不等)
            return False
        return self.is_subtree(A.left,B.left) and self.is_subtree(A.right,B.right)                                              #如果B是A的子树，那么B.left是A.left的子树并且B.right是A.right的子树
            
if __name__ == "__main__":
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.left = TreeNode(3)
    
    tree2 = TreeNode(4)
    tree1.left.left = tree2
    tree2.left = TreeNode(11)
    tree2.right = TreeNode(12)

    print tree1.printNode(tree1)
    print tree2.printNode(tree2)
    print Solution().HasSubtree(tree1,tree2)
    
