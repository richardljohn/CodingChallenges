class Node: 
    def __init__(self, val):
        self.val = val
        self.next = None

def sumList(head):
    if head is not None: 
        sum = 0
        curr = head
        while curr is not None: 
            sum += curr.val
            curr = curr.next
        return sum
    return 0 


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d


print(sumList(a))