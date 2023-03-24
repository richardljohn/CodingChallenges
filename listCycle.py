# LeetCode #141 - Linked List Cycle 

# Definition for singly-linked list.
class Node(object):
     def __init__(self, x):
         self.val = x
         self.next = None

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

#Test Cases 
a = Node(3)
b = Node(2)
c = Node(0)
d = Node(4)
a.next = b
b.next = c
c.next = d
d.next = b
print(hasCycle(a))