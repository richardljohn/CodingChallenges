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
            
            result = max(result, r - l - 1)
        
        return result

S = Solution()

# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

print(S.characterReplacement("ABAB", 2))

# Example 2:
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
