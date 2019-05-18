# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def Merge1(self, pHead1, pHead2):                                 #额外空间复杂度O(1),时间复杂度O(m+n)
        """非递归版本"""
        if pHead1 == None or pHead2 == None:                         #处理空链表
            return pHead1 if pHead2 == None else pHead2
        if pHead1.val < pHead2.val:                                  #确定起始位置,cur1指向两个链表中的最小值节点
            cur1,cur2,pre = pHead1,pHead2,None
        else:
            cur1,cur2,pre = pHead2,pHead1,None
        while cur1.next != None and cur2 != None:
            if cur1.next.val > cur2.val:                        
                temp = cur2.next
                cur2.next = cur1.next
                cur1.next = cur2
                pre = cur2
                cur1 = cur2.next
                cur2 = temp
            else:
                pre = cur1
                cur1 = cur1.next
        if cur1.next == None and cur2 != None:                       #cur1指针指向尾节点,cur2不为空
            if cur1.val <= cur2.val:
                cur1.next = cur2
            else:
                cur2.next = cur1
                pre.next = cur2
        return pHead1 if pHead1.val < pHead2.val else pHead2

    def Merge2(self,pHead1,pHead2):
        """递归版本"""
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1
        if pHead1.val <= pHead2.val:
            pHead1.next = self.Merge2(pHead1.next,pHead2)
            return pHead1
        else:
            pHead2.next = self.Merge2(pHead2.next,pHead1)
            return pHead2
        
    def printNode(self,node):                                        #测试函数
        if node is None:
            return
        while node != None:
            print node.val,
            node = node.next

if __name__ == "__main__":
    listNode1 = ListNode(1)
    listNode1.next = ListNode(3)
    listNode1.next.next = ListNode(7)

    listNode2 = ListNode(2)
    listNode2.next = ListNode(4)
    listNode2.next.next = ListNode(6)

    listNode3 = None
    solution = Solution()
    mergeNode = solution.Merge2(listNode1,listNode2)
    solution.printNode(mergeNode)
            
