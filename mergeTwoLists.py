# Leetcode #21 - Merge Two Sorted Lists

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummyHead = ListNode(0)
        head = dummyHead
        headOne, headTwo = list1, list2

        while headOne is not None and headTwo is not None:
            if headOne.val > headTwo.val: 
                dummyHead.next = ListNode(headOne.val)
                headOne = headOne.next
                dummyHead = dummyHead.next
            else:
                dummyHead.next = ListNode(headTwo.val)
                headTwo = headTwo.next
                dummyHead = dummyHead.next
        
        if headOne is None:
            dummyHead.next = headTwo
        if headTwo is None: 
            dummyHead.next = headOne
        
        return head.next
