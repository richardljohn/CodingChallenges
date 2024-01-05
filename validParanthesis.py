# Leetcode #20 - Valid Paranthesis (Done)

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        l, end = 0, len(s)
        
        stack = []
        brackets = { ")" : "(", "]" : "[", "}": "{" } # Each bracket must match

        for c in s: 
            if c in brackets: 
                if stack and stack[-1] == brackets[c]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False