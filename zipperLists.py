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
d.next = e

def zipperLists(headOne, headTwo):
    if headOne == None or headTwo == None:
        return
    
    currOne, currTwo = headOne, headTwo
    count = 1
    newHead = Node(currOne.val)
    currOne = currOne.next
    count += 1
    while currOne.next != None and currTwo.next != None: 
        if count % 2 == 0: 
            newHead.next = currTwo
            count += 1
            newHead = newHead.next
            currTwo = currTwo.next
        if count % 2 == 1: 
            newHead.next = currOne
            count += 1
            newhead = newHead.next
            currOne = currOne.next
    if currOne.next == None: 
        curr = currTwo
        while curr != None: 
            newHead.next = curr 
            newHead = newHead.next
            curr = curr.next
    if currTwo.next == None: 
        curr = currOne
        while curr != None: 
            newHead.next = curr 
            newHead = newHead.next
            curr = curr.next
    return newHead

print(zipperLists(a, d))




# Pseudocode. 
# Make a new list
# Traverse both lists. 
# While you can traverse both the lists further. Add the current node to the new linked list
# If you cant traverse both of the lists, end.