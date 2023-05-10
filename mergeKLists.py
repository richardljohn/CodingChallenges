# Leetcode 23 - Merge K Sorted Lists

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

    
    def mergeLists(self, listOne, listTwo):
        dummy = ListNode(None)
        tail = dummy 
        currOne = listOne
        currTwo = listTwo
        
        while currOne is not None and currTwo is not None: 
            if currOne.val > currTwo.val:
                tail.next = currTwo
                currTwo = currTwo.next
                tail = tail.next
            else:
                tail.next = currOne
                currOne = currOne.next
                tail = tail.next
        
        if currOne is None:
            tail.next = currTwo
        if currTwo is None:
            tail.next = currOne
        
        return dummy.next