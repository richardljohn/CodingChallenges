class Node: 
    def __init__(self, val):
        self.val = val
        self.next = None


def zippperLists(headOne, headTwo):
    
    tail = headOne
    currOne = headOne.next
    currTwo = headTwo
    count = 0

    while currOne is not None and currTwo is not None: 
        if count % 2 == 0: 
            tail.next = headTwo
            headTwo = headTwo.next
        else: 
            tail.next = headOne
            headOne = headOne.next
        count += 1
        tail = tail.next

    if currOne is None: 
        tail.next = currTwo
    
    if currTwo is None: 
        tail.next = currOne

    return headOne

# Pseudocode. 
# Make a new list
# Traverse both lists. 
# While you can traverse both the lists further. Add the current node to the new linked list
# If you cant traverse both of the lists, end.