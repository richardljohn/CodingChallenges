# Leetcode 28. Find the Index of the First Occurrence in a String

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(haystack) < len(needle): 
            return -1
        
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                 return i
        return -1

# Test
S = Solution()
print(S.strStr("leetcode", "leeto"))
print(S.strStr("samsaidhi", "hi"))
print(S.strStr("letterman", "let"))