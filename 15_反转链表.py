# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def ReverseList(self, pHead):
        if pHead is None:
            return
        cur,pre = pHead,None
        while cur != None:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
