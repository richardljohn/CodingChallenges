# Leetcode 206 - Reverse Linked List

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e

while a is not None:
    print(str(a.val) + " ->", end=" ")
    a = a.next
print("None")

s = Solution()
ans = s.reverseList(a)

while ans is not None:
    print(str(ans.val) + " ->", end=" ")
    ans = ans.next
print("None")

