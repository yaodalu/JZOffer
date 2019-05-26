# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

    def printNext(self,x):                                                      #测试函数
        while x != None:
            print x.label,
            x = x.next
            
    def printRandom(self,x):                                                    #测试函数
        while x != None: 
            if x.random:
                print (x.label,x.random.label),
            x = x.next
            
class Solution:
    def Clone(self, pHead):
        """Dict隐射版本"""                                                       #空间复杂度O(n),时间复杂度O(n)
        copyDict,cur = {},pHead
        while cur != None:                                                      #创建节点-新节点的映射copyDict
            copyDict[cur] = RandomListNode(cur.label)
            cur = cur.next
        for i in copyDict.keys():
            copyDict[i].next = i.next
            copyDict[i].random = i.random
        return copyDict[pHead]

    def Clone2(self,pHead):                                                     #空间复杂度O(1),时间复杂度O(n)
        """分离新旧节点版本"""
        cur = pHead
        while cur != None:                                                      #在每个节点后链接上复制节点
            temp = RandomListNode(cur.label)
            temp.next = cur.next
            cur.next = temp
            cur = cur.next.next
        cur = pHead
        while cur != None:                                                      #复制随机指针
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        newpHead = pHead.next                                                   #分离新旧节点
        cur = newpHead                 
        while cur.next != None:                                                 #注意终止条件,退出循环时,cur指向最后一个复制节点
            temp = cur.next.next
            cur.next = temp
            cur = temp
        return newpHead

if __name__ == "__main__":
    randomListNode = RandomListNode(1)
    randomListNode.next = RandomListNode(2)
    randomListNode.next.next = RandomListNode(3)
    randomListNode.next.next.next = RandomListNode(4)
    randomListNode.random = randomListNode.next.next

    new = Solution().Clone2(randomListNode)
    new.printNext(new)
    new.printRandom(new)
