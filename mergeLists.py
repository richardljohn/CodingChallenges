class Node: 
    def __init__(self, val):
        self.val = val
        self.next = None


def merge_lists(headOne, headTwo):
    dummyHead = Node(None)
    tail = dummyHead
    currOne, currTwo = headOne, headTwo

    
    while currOne is not None and currTwo is not None: 
        if currOne.val > currTwo.val: 
            tail.next = currTwo
            currTwo = currTwo.next
        else: 
            tail.next = currOne
            currOne = currOne.next
        tail = tail.next
    
    if currOne is None: 
        tail.next = currTwo
    if currTwo is None: 
        tail.next = currOne

    return dummyHead.next
    


a = Node(5)
b = Node(7)
c = Node(10)
d = Node(12)
e = Node(20)
f = Node(28)
g = Node(32)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
# 5 -> 7 -> 10 -> 12 -> 20 -> 28

q = Node(6)
r = Node(8)
s = Node(9)
t = Node(25)
q.next = r
r.next = s
s.next = t
# 6 -> 8 -> 9 -> 25

n = merge_lists(a, q)

while n is not None: 
    print(str(n.val) + " ->", end=" ")
    n = n.next
print("None")  
# 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 12 -> 20 -> 25 -> 28


# Pseudocode. 
# Two Pointers. One for each List. Tail. Point it to the shorter of the two lists.
# Compare both pointers. 
# Whichever has the smaller value, insert into the new LinkedList. 
# Continue until both lists are finsihed. 
# If one list is none, add all of the other list and return the head. 
# If the other is none, add the other.  
# Output is good.
# Properly Working.
#
#