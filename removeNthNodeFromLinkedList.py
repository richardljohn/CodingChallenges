# Leetcode #19 - Remove Nth Node From End of List

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        left = dummy 
        right = head 

        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right: 
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next

s = Solution()
# Test Cases 
head = ListNode([1,2,3,4,5])
n = 2
print(s.removeNthFromEnd(head, n))

head = ListNode([1])
n = 1
print(s.removeNthFromEnd(head, n))

head = ListNode([1,2])
n = 1
print(s.removeNthFromEnd(head, n))