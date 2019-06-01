# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        """单向循环链表解法"""
        if n == 0:                                              #特殊情况,没有小朋友
            return -1
        if n == 1:                                              #特殊情况,只有一个小朋友
            return 1
        if m == 1:                                              #特殊情况,每次第一个小朋友退出
            return n-1
        myList = MyList(n)
        while not myList.judgeOneElem():
            myList.pop(m)
        return myList.judgeOneElem().val

class Node():
    def __init__(self,val):
        self.val = val
        self.next = None

class MyList():
    """尾指针指向头节点的单向循环链表"""    
    def __init__(self,n):                                       #n>=2
        self.__head = Node(0)
        cur = self.__head
        for i in range(1,n-1):                                  #退出循环时,cur指向倒数第二个节点
            cur.next = Node(i)
            cur = cur.next
        cur.next = Node(n-1)
        cur = cur.next
        cur.next = self.__head
    
    def judgeOneElem(self):
        """判断链表是否只有一个节点"""                         
        if self.__head and self.__head.next == self.__head:  
            return self.__head                                  #如果链表只有一个节点,则返回该节点
        return False
    
    def pop(self,m):
        """遍历"""
        if self.__head is None:
            return
        cur,count = self.__head,0
        while count != m-2 :                                    #退出循环的时候，指针指向需要删除的节点的前一个节点
            cur = cur.next
            count += 1
        self.__head = cur.next.next                             #头节点指向删除节点的后一个节点
        cur.next = self.__head

if __name__ == "__main__":
    print Solution().LastRemaining_Solution(5,3)
        
