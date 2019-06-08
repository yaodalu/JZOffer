# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
        
class Solution:
    def GetNext(self, pNode):                                                                                                               
        """中序遍历递归版本"""
        fatherNode = self.getFatherNode(pNode)                                                                          
        inOrderList = self.inOrderRecur(fatherNode)
        return inOrderList[inOrderList.index(pNode)+1] if inOrderList.index(pNode) < len(inOrderList)-1 else None       #防止溢出

    def inOrderRecur(self,fatherNode,inOrderList = []):
        """得到中序遍历的节点列表"""
        if not fatherNode:
            return 
        self.inOrderRecur(fatherNode.left,inOrderList)
        inOrderList += [fatherNode]
        self.inOrderRecur(fatherNode.right,inOrderList)
        return inOrderList                                                                                              #此处返回inOrderList是为了和调用语句inOrderList = self.inOrderRecur(fatherNode)相对应，若不返回，inOrderList中也记录了中序遍历

    def getFatherNode(self,pNode):
        """寻找根节点"""
        if not pNode.next:
            return pNode
        fatherNode = self.getFatherNode(pNode.next)
        return fatherNode

    def GetNext1(self,pNode):
        """一步到位版本"""
        if pNode.right:                                                                                                 #如果该节点有右子树,那么下一个节点是右子树的最左的节点
            cur = pNode.right
            while cur.left:
                cur = cur.left 
            return cur
        else:
            while pNode.next:                                                                                           
                father = pNode.next
                if father.left == pNode:                                                                                #若该节点没有右子树，若该节点是父节点的左节点，返回父节点，若不是则继续往上走，直到满足退出，默认返回None
                    return father                                                                                   
                pNode = father

if __name__ == "__main__":
    tree = TreeLinkNode(1)                                                                                              #中序遍历顺序:7->4->8->2->5->1->3->6
    tree.left = TreeLinkNode(2)
    tree.right = TreeLinkNode(3)
    tree.left.left = TreeLinkNode(4)
    tree.left.right = TreeLinkNode(5)
    tree.right.right = TreeLinkNode(6)
    tree.left.left.left = TreeLinkNode(7)
    tree.left.left.right = TreeLinkNode(8)
    
    tree.left.next = tree                                                                                               #定义指向父节点的指针next
    tree.right.next = tree  
    tree.left.left.next = tree.left
    tree.left.right.next = tree.left
    tree.right.right.next = tree.right
    tree.left.left.left.next = tree.left.left
    tree.left.left.right.next = tree.left.left

    solution = Solution()
    nextNode = solution.GetNext1(tree.right.right)
    print nextNode
    
    
