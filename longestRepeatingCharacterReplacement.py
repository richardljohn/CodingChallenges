# Leetcode #424 - Longest Repeating Character Replacement

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        charMap = {}
        result = 0

        l = 0 
        
        for r in range(len(s)):
            charMap[s[r]] = 1 + charMap.get(s[r], 0)

            while (r - 1 + 1) - max(charMap.values()) > k: 
                charMap[s[l]] -= 1
                l += 1
            
            res = max(res, r - l - 1)
        
        return res

S = Solution()