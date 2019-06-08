# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def EntryNodeOfLoop(self, pHead):
        if pHead is None or pHead.next is None or pHead.next.next is None:
            return None
        slow,fast = pHead.next,pHead.next.next                                  #slow,fast初始值不同

        while slow != fast:                                                     #两指针相遇退出循环，快指针多走的步数为环的长度?
            if fast is None or fast.next is None or fast.next.next is None:
                return None
            slow = slow.next
            fast = fast.next.next
            
        fast = pHead                                                            
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow

if __name__ == "__main__":
    ll1 = ListNode(1)                                                           #无环链表 1->2->3->4
    ll1.next = ListNode(2)
    ll1.next.next = ListNode(3)
    ll1.next.next.next = ListNode(4)

    ll2 = ListNode(1)                                                           #有环链表 1->2->3->4->5->3
    ll2.next = ListNode(2)
    ll2.next.next = ListNode(3)
    ll2.next.next.next = ListNode(4)
    ll2.next.next.next.next = ListNode(5)
    ll2.next.next.next.next.next = ll2.next.next

    print Solution().EntryNodeOfLoop(ll2).val
