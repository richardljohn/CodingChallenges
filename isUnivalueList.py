class Node: 
    def __init__(self, val):
        self.val = val
        self.next = None


def is_univalue_list(head):
    target = head.val
    curr = head
    while curr is not None: 
        if curr.val != target:
            return False
        curr = curr.next

    return True

a = Node(7)
b = Node(7)
c = Node(7)
d = Node(7)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e

print(is_univalue_list(a))