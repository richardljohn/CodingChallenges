# Leetcode #9 - Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        num = str(x)

        return num == num[::-1]

S = Solution()

print(S.isPalindrome(975)) # False
print(S.isPalindrome(121)) # True
print(S.isPalindrome(-121)) # False