class Node: 
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e

def reverseList(head):
    prev = None 
    curr = head 
    while curr is not None: 
        next = curr.next
        curr.next = prev
        prev = curr 
        curr = next
    return prev