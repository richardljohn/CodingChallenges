class Node: 
    def __init__(self, val):
        self.val = val
        self.next = None

def sumList(head):
    sum = 0 
    while head is not None:
        sum += int(head.val)
        head = head.next
    return sum

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d


print(sumList(a))