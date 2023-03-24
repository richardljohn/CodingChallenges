# LeetCode #141 - Linked List Cycle 

#class Solution(object):
def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    visited = set()

    while head != None:
        if head in visited:
            return True
        visited.add(head)
        head = head.next
    return False