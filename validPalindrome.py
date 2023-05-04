# Leetcode 125 - Valid Palindrome

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
    
        word = ""
        i = 0
        while i < len(s):
            if s[i].isalpha():
                word += s[i].lower()
                i += 1
            else: 
                i += 1
        
        if word == word[::-1]:
            return True
        else:
            return False


s = Solution()
print(s.isPalindrome("0P"))
print(s.isPalindrome("Racecar"))