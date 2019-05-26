# -*- coding:utf-8 -*-
import pdb
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if not root:
            return []
        if root and not root.left and not root.right and root.val == expectNumber:                              #叶节点的值为expectNumber
            return [[root.val]]                                                                                 #叶节点的个数和为最大可能的路径数和,对应left+right
        res = []                                                                                                #如果left和right均为[],res直接返回[]
        left = self.FindPath(root.left, expectNumber-root.val)                                                  
        right = self.FindPath(root.right, expectNumber-root.val)                            
        for i in left+right:                                                                                    #回溯
            res.append([root.val]+i)                                                                        
        return res
                

if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)
##    pdb.set_trace()
    print Solution().FindPath(tree,2)
        
