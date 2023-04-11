# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nonDupes = []
        nodes = set()
        curr = head 

        while curr is not None: 
            if curr in nodes: 
                curr = curr.next
            else: 
                nodes.add(curr)
                nonDupes.append(curr.val)
                curr = curr.next
        return nonDupes