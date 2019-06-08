# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):                     
        if not pRoot:                               
            return []
        nodeList = []
        nodeList,height = self.levelOrder(pRoot,nodeList)
        count,res = 0,[]
        for i in range(height+1):
            res.append([])
        for node,layer in nodeList:
            if count != layer:
                count += 1
                res[count].append(node.val)
            else:
                res[count].append(node.val)
        return res
        
    def levelOrder(self,pRoot,nodeList):
        """层次遍历"""
        queue = [(pRoot,0)]
        while len(queue) >= 1:
            node,layer = queue.pop(0)
            nodeList += [(node,layer)]
            if node.left:
                queue.append((node.left,layer+1))
            if node.right:
                queue.append((node.right,layer+1))            
        return nodeList,layer

if __name__ == "__main__":
    tree = TreeNode(8)
    tree.left = TreeNode(6)
    tree.right = TreeNode(6)
    tree.left.left = TreeNode(5)
    tree.left.right = TreeNode(7)
    tree.right.left = TreeNode(7)
    tree.right.right = TreeNode(5)

    print Solution().Print(tree)
    
