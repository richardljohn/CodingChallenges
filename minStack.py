# Leetcode 151 - Min Stack

class MinStack(object):

    def __init__(self):
        self.mainStack = []
        self.minStack = []
        
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.mainStack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        self.mainStack.pop()
        self.minStack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.mainStack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin()) # return -3
minStack.pop()
print(minStack.top() )   # return 0
print(minStack.getMin()) # return -2
