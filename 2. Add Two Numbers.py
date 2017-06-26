# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''


# the hard part of this is you have to create a root = list
# so that in the end of the function, it could return the ListNode from beginning
# http://www.openbookproject.net/thinkcs/python/english2e/ch18.html
# the page listed above help in understanding ListNode


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        list = ListNode(0)
        root = list
        store = 0
        while l1 or l2 or store:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            val = (v1 + v2 + store) % 10
            store = (v1 + v2 + store) // 10
            list.next = ListNode(val)
            list = list.next

        return root.next

        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
