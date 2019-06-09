# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Serialize(self,root):
        """二叉树序列化得到前序遍历数组"""
        return self.preOrderSerialize(root)

    def Deserialize(self, s):
        """前序遍历数组反序列化得到二叉树"""
        if not s:
            return
        return self.deserializeRecur(s)

    def deserializeRecur(self,s,root=None):
        flag,number = self.readStream(s)
        if flag:
            root = TreeNode(number)                                     #建立二叉树的顺序，和前序遍历顺序一致，先根节点，后左，最后右
            root.left = self.deserializeRecur(s,root.left)              #当root为叶节点,root.left为None  self.deserializeRecur(s,root.left)返回值为None       
            root.right = self.deserializeRecur(s,root.right)            
        return root
            
    def readStream(self,s):
        """遍历返回前序遍历结果"""
        flag,number = True,s.pop(0)
        if number == '#':
            flag = False
        return flag,number

    def preOrderSerialize(self,root,res=[]):
        if not root:
            res.append('#')
            return res
        res.append(root.val)
        self.preOrderSerialize(root.left,res)
        self.preOrderSerialize(root.right,res)
        return res


if __name__ == "__main__":
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)
    tree1.left.left = TreeNode(4)
    tree1.right.left = TreeNode(5)
    tree1.right.right = TreeNode(6)

    solution = Solution()
    s =  solution.Serialize(tree1)
    root = solution.Deserialize(s)
    newS = solution.Serialize(root)
    print newS == s
