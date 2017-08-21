# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        if not head:
            return []
        elif head.next == None:
            return head

        result = head
        list_of_element = []
        while head.next:
            list_of_element.append(head.val)
            head = head.next
        list_of_element.append(head.val)
        lenth = len(list_of_element)
        if k % lenth == 0 or k == 0:
            return result
        else:
            position_change = k % lenth
            list_of_element = list_of_element[-position_change:] + list_of_element[:-position_change]
        print(list_of_element)
        return_result = result
        index = 0
        while result.next:
            result.val = list_of_element[index]
            index += 1
            result = result.next
        result.val = list_of_element[index]
        return return_result

        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
