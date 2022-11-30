class Node: 
    def __init__(self, val):
        self.val = val
        self.next = None

def longest_streak(head):
    if head is None: 
        return None
    
    currStreak = 0
    maxStreak = 0
    curr = head
    prev = None

    while curr is not None: 
        if curr.val == prev:
            currStreak += 1
        else: 
            currStreak = 1
        
        prev = curr.val
        if currStreak > maxStreak:
            maxStreak = currStreak
        
        curr = curr.next
    
    return maxStreak


a = Node(3)
b = Node(0)
c = Node(3)
d = Node(0)
e = Node(1)

a.next = b
b.next = c
c.next = d
d.next = e


print(longest_streak(a))