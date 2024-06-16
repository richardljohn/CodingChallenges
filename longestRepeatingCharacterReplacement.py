# Leetcode #424 - Longest Repeating Character Replacement (Done)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # Hash Map
        count = {}
        # Max Window 
        res = 0
        # Sliding Window
        l = 0
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res

S = Solution()
string = "AAABABA"
k = 2
print(S.characterReplacement(string, k))