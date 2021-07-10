"""输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    
    def reversePrint(self, head: ListNode):
        list_new = []
        list_final = []
        while head:
            list_new.append(head.val)
            head = head.next
        for i in range(len(list_new)):
            list_final.append(list_new[len(list_new) - i - 1])
        return list_final

