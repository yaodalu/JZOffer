# -*- coding: utf-8 -*-
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def printListFromTailToHead1(self,listNode):                                        #利用栈的先进后出
        temp,res = [],[]                                                                #额外空间复杂度O(n)
        while listNode:
            temp.append(listNode.val)                                                   #temp中存储正向链表值
            listNode = listNode.next
        while temp:
            res.append(temp.pop())                                                      #res中存储反向链表值
        return res

    def printListFromTailToHead2(self,listNode):                                        #反转链表指针
        res = []                                                                        #额外空间复杂度O(1)
        cur,pre = listNode,None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp                                                                  #循环结束时,链表反向,pre指向尾节点
        while pre:
            res.append(pre.val)
            pre = pre.next
        return res

    def printListFromTailToHead3(self,listNode):                                        #方法1的递归版本
        if not listNode:
            return []
        return self.printListFromTailToHead3(listNode.next)+[listNode.val]              #用+代替append

    def printListFromTailToHead4(self,listNode):                                        #方法1的错误递归版本
        if not listNode:
            return []
        return self.printListFromTailToHead4(listNode.next).append(listNode.val)        #a.append(1)无返回值
            
        
if __name__ == "__main__":
    listNode = ListNode(1)
    listNode.next = ListNode(2)
    listNode.next.next = ListNode(3)
    solution = Solution()
    print solution.printListFromTailToHead4(listNode)
    
            
