# -*- coding:utf-8 -*-
class Node():
    def __init__(self,val):
        self.val = val
        self.next = None

class MyList():                                             #尾指针指向头节点的单向链表                   
    def __init__(self):
        self.__head = None

    def add(self,item):                                    
        """尾插元素"""
        if self.__head is None:
            node = Node(item)
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            node = Node(item)
            while cur.next != self.__head:                 #退出循环时,cur指针指向尾节点
                cur = cur.next
            cur.next = node
            node.next = self.__head

    def travel(self):
        """遍历"""
        if self.__head is None:
            return
        cur = self.__head
        res = ""
        while cur.next != self.__head:
            res += cur.val
            cur = cur.next
        res += cur.val
        return res

    def leftRotate(self,n):
        count = 0
        cur = self.__head
        while count < n:                                  #退出循环时，cur指针指向新的头节点
            cur = cur.next
            count += 1
        self.__head = cur
        return self.travel()
    
class Solution:
    def LeftRotateString1(self, s, n):                                 
        """带尾指针的单向链表"""
        if not s:
            return ''
        myList = MyList()
        for item in s:
            myList.add(item)
        return myList.leftRotate(n)

     def LeftRotateString2(self, s, n):
         """字符串操作"""
        if not s:                                        #空字符串不为None?
            return ''
        diff = n%len(s)
        return s[diff:]+s[:diff]                         #字符串拼接与切片
    
if __name__ == "__main__":
    print Solution().LeftRotateString('abcdefg',2)
