# Leetcode 125 - Valid Palindrome

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
    
        l, r = 0, len(s) - 1
        while l < r: 
            while l < r and not self.isAlphaOrNum(s[l]):
                l += 1
            while r > l and not self.isAlphaOrNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True 

    def isAlphaOrNum(self, c):
        return ( ord('A') <= ord(c) <= ord('Z') or 
        ord('a') <= ord(c) <= ord('z') or 
        ord('0') <= ord(c) <= ord('9'))

s = Solution()
print(s.isPalindrome("0P"))
print(s.isPalindrome("Racecar"))