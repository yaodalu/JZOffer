# -*- coding:utf-8 -*-
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
        # write code here
        if not pHead:                                   
            return
        if not pHead.next:                                               #单个节点
            return pHead
        if not pHead.next.next:
            return pHead if pHead.val != pHead.next.val else None        #两个节点
            
        pre,cur,last = None,pHead,pHead.next                             #长度>=2的链表，
        while last != None:
            if cur.val == last.val:
                while last != None and cur.val == last.val:
                    last = last.next
                if not last:                                            #例如12222
                    if pre:
                        pre.next = None
                        break
                    else:
                        return None
                if not last and cur.val == last.val:                    #例如122223
                    if pre:
                        pre.next = last
                        break
                if last and cur.val != last.val:                        #例如122334
                    if cur == pHead and not last.next:
                        return last
                    else:
                        cur,last = last,last.next
                        pre.next = cur
            else:
                pre,cur,last = cur,last,last.next
        return pHead 

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

    node = ListNode(1)
    node.next = ListNode(1)
    node.next.next = ListNode(1)
    node.next.next.next = ListNode(1)
    node.next.next.next.next = ListNode(1)
    newNode = Solution().deleteDuplication(node)
    node.printNode(newNode)

