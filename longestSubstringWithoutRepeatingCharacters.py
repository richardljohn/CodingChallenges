# Leetcode #3 - Longest Substring Without Repeating Characters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        maxString = 0
        l, r = 0, 0
        characters = set()

        while r < len(s):
            stringLength = 0
            if s[r] not in characters: 
                characters.add(s[r])
                stringLength += 1
            else: 
                characters.clear()
                maxString = max(maxString, stringLength)
            r += 1
            l = r
        return maxString

S = Solution()

#Testcases
print(S.lengthOfLongestSubstring("abcabcbb"))
print(S.lengthOfLongestSubstring("bbbbb"))
print(S.lengthOfLongestSubstring("pwwkew"))