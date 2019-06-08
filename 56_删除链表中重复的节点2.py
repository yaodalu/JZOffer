# -*- coding: utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def printNode(self,node):
        if not node:
            print None
        while node != None:
            print node.val,
            node = node.next
        print '\n'

class Solution:
    def deleteDuplication(self, pHead):
        if not pHead:                                   
            return
        if not pHead.next:                                               #特殊情况:单个节点
            return pHead
        if not pHead.next.next:
            return pHead if pHead.val != pHead.next.val else None        #特殊情况:两个节点

        newHead = ListNode(0)                                            #创建新的头节点,使得如(1,1,1,1)为空
        newHead.next = pHead
        pre,last = newHead,newHead.next
        while last != None:
            if last.next != None and last.val == last.next.val:
                while last.next != None and last.val == last.next.val:  #退出循环时，last为最后一个节点或者出现值不同
                    last = last.next
                pre.next = last.next                                    #删除重复节点last
                last = last.next
            else:
                pre = pre.next
                last = last.next
        return newHead.next

if __name__ == "__main__":
##    node = ListNode(1)
##    node.next = ListNode(2)
##    node.next.next = ListNode(3)
##    node.next.next.next = ListNode(3)
##    node.next.next.next.next = ListNode(4)
##    node.next.next.next.next.next = ListNode(4)
##    node.next.next.next.next.next.next = ListNode(5)
##
##    node.printNode(node)
##    newNode = Solution().deleteDuplication(node)
##    newNode.printNode(newNode)

    node = ListNode(0)
    node.next = ListNode(0)
    node.next.next = ListNode(0)
    node.next.next.next = ListNode(0)
    node.next.next.next.next = ListNode(0)
    newNode = Solution().deleteDuplication(node)
    node.printNode(newNode)
