# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail1(self,head,k):                #额外空间复杂度O(n)
        """列表法"""
        if head is None or k == 0:                  
            return
        temp,count = [],0
        while head != None:
            temp.append(head)
            head = head.next
            count += 1
        if count < k:
            return
        return temp[-k]

    def FindKthToTail2(self,head,k):                #空间复杂度O(1)
        """等间隔法"""
        if head is None or k == 0:                  #防止空链表,init_k=1    
            return
        slow,fast,count = head,head,1
        while count < k:                            #等间隔法:第1个节点和第k个节点的间隔,等于最后一个节点和倒数第k个节点的间隔
            count += 1
            fast = fast.next
        if fast is None:                            #防止溢出
            return
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        return slow
            
if __name__ == "__main__":
    listNode = ListNode(1)
    listNode.next = ListNode(2)
    listNode.next.next = ListNode(3)
    listNode.next.next.next = ListNode(4)
    listNode.next.next.next.next = ListNode(5)
    print Solution().FindKthToTail1(listNode,6)
        
        
