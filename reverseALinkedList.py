# Leetcode 206 - Reverse Linked List

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        inFront = head.next

        while curr is not None:
            curr.next = prev
            prev = curr
            curr = inFront
            inFront = inFront.next
        return curr