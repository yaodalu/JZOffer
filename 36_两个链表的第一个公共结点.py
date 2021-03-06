# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if pHead1 == None or pHead2 == None:
            return None
        loop1 = self.getLoopNode(pHead1)
        loop2 = self.getLoopNode(pHead2)
        if (loop1 == None) and (loop2 == None):         #有环单向链表与无环单向链表不可能相交
            return self.noLoop(pHead1,pHead2)
        if (loop1 != None) and (loop2 != None):
            return self.bothLoop(pHead1,pHead2,loop1,loop2)

    def getLoopNode(self,node):
        """判断链表是否有环，有则返回入环节点"""
        if node:                                #特殊情况判断
            if node.next:
                if not node.next.next:
                    return None
            else:
                return None
        else:
            return None
        slow = node.next
        fast = node.next.next
        while (fast != slow):
            if fast.next != None:
                if fast.next.next != None:
                    fast = fast.next.next
                    slow = slow.next
                else:
                    return None                         #fast指针指向空则无环
            else:
                return None
        fast = node                                     #fast指针和slow指针相遇后，fast指针指向头节点
        while (fast != slow):
            fast = fast.next                            #fast指针走一步
            slow = slow.next                            #slow指针走一步
        return fast                                     #两个指针相遇的节点即为入环节点

    def noLoop(self,node1,node2):
        """两个无环的链表的相交问题"""
        cur1 = node1
        cur2 = node2
        count = 0
        while cur1.next != None:                        #退出循环时，cur1指针指向node1链表的尾节点
            count += 1
            cur1 = cur1.next
        while cur2.next != None:
            count -= 1
            cur2 = cur2.next
        if cur1 != cur2:                                #两个无环单向链表相交，一定是"Y"形
            return None
        if count >= 0:                          
            cur1,cur2 = node1,node2
        else:
            cur1,cur2 = node2,node1
        count = abs(count)
        while (count != 0):                             #长度较长的链表先走
            count -= 1
            cur1 = cur1.next
        while (cur1 != cur2):
            cur1,cur2 = cur1.next,cur2.next
        return cur1
        
    def bothLoop(self,node1,node2,loop1,loop2):
        """两个有环链表的相交问题"""
        if (loop1 == loop2):                            #入环节点相同为"Y加圈"形式
            cur1 = node1
            cur2 = node2
            count = 0
            while cur1 != loop1:                                             
                count += 1
                cur1 = cur1.next
            while cur2 != loop2:
                count -= 1
                cur2 = cur2.next
            if cur1 != cur2:                                
                return None
            if count >= 0:                          
                cur1,cur2 = node1,node2
            else:
                cur1,cur2 = node2,node1
            count = abs(count)
            while (count != 0):                             
                count -= 1
                cur1 = cur1.next
            while (cur1 != cur2):
                cur1,cur2 = cur1.next,cur2.next
            return cur1
        else:                                       #入环节点不同为"V加圈"形式
            cur1 = loop1.next
            while cur1 != loop1:                    
                if cur1 == loop2:                   #判断loop2是否在node1的环上，若在则相交
                    return loop1
                else:
                    cur1 = cur1.next
            return None

if __name__ == "__main__":
    ll1 = ListNode(1)                                       #无环链表 1->2->3->4
    ll1.next = ListNode(2)
    ll1.next.next = ListNode(3)
    ll1.next.next.next = ListNode(4)

    ll2 = ListNode(1)                                       #有环链表 1->2->3->4->5->3
    ll2.next = ListNode(2)
    ll2.next.next = ListNode(3)
    ll2.next.next.next = ListNode(4)
    ll2.next.next.next.next = ListNode(5)
    ll2.next.next.next.next.next = ll2.next.next

    ll3 = ListNode(1)                                       #有环链表 1->2->3->4->3
    ll3.next = ListNode(2)
    ll3.next.next = ListNode(3)
    ll3.next.next.next = ListNode(4)
    ll3.next.next.next.next = ll3.next.next

    print Solution().getLoopNode(ll1) is None
    print Solution().getLoopNode(ll2).val
    print Solution().getLoopNode(ll3).val

    print Solution().FindFirstCommonNode(ll2,113)

        
