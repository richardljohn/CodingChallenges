# Leetcode 125 - Valid Palindrome

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
    
        s = ""
        i = 0
        while i < len(s):
            if s[i].isalpha():
                s += s[i].lower()
                i += 1
            else: 
                i += 1
        