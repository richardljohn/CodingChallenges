# Leetcode #9 - Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        num = str(x)

        return num == num[::-1]

S = Solution()

print(S.isPalindrome(975))
print(S.isPalindrome(121))
print(S.isPalindrome(-121))