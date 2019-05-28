# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def TreeDepth(self, pRoot):
        """求层次遍历"""
        if not pRoot:
            return 0
        if pRoot and pRoot.left is None and pRoot.right is None:
            return 1
        queue = [(pRoot,1)]
        while len(queue) :
            node,layer = queue.pop(0)
            if node.left not in queue and node.left is not None:
                queue.append((node.left,layer+1))
            if node.right not in queue and node.right is not None:
                queue.append((node.right,layer+1))
        return layer
    
if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    tree.left.left.right = TreeNode(7)
    print Solution().TreeDepth(tree)
            
