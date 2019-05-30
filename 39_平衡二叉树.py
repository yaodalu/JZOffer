# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def IsBalanced_Solution(self, pRoot): 
        if not pRoot:                                                                                                           #不懂?
            return True
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right) and abs(self.countLayer(pRoot.left)-self.countLayer(pRoot.right)) <= 1
            
    def countLayer(self, pRoot):
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
    tree1 = TreeNode(1)                                             #tree1是不平衡二叉树
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)
    tree1.left.left = TreeNode(4)
    tree1.left.right = TreeNode(5)
    tree1.left.left.left = TreeNode(6)
 
    tree2 = TreeNode(1)                                             #tree2是平衡二叉树
    tree2.left = TreeNode(2)
    tree2.right = TreeNode(3)
    tree2.left.left = TreeNode(4)
    tree2.left.right = TreeNode(5)
    tree2.right.left = TreeNode(6)

    print Solution().IsBalanced_Solution(tree1)
    print Solution().IsBalanced_Solution(tree2)
