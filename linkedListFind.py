class Node: 
    def __init__(self, val):
        self.val = val
        self.next = None
        

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

def linkedListFind(head, target):
    if head is not None:
        curr = head 
        while curr is not None: 
            if curr.val == target:
                return True 
            curr = curr.next
        return False 
    return False