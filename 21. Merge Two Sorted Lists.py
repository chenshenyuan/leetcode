# this is not totally original work of me, I checked the answer and write myself


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        result = process = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                process.next = l1
                l1 = l1.next
            else:
                process.next = l2
                l2 = l2.next
            process = process.next
        process.next = l1 or l2
        return result.next

        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """