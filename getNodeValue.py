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

def getNodeValue(head, index):
    if head is not None:
        counter = 0
        curr = head
        while curr is not None and counter <= index: 
            if counter == index:
                return curr.val
            curr = curr.next
            counter += 1
        return 

print(getNodeValue(a, 0))
print(getNodeValue(a, 1))
print(getNodeValue(a, 2))
print(getNodeValue(a, 3))