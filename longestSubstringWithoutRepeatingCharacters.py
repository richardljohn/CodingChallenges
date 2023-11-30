# Leetcode #3 - Longest Substring Without Repeating Characters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        l = 0
        maxString = 0
        characters = set()

        for r in range(len(s)):
            while s[r] in characters: 
                characters.remove(s[l])
                l += 1
            characters.add(s[r])
            maxString = max(maxString, r - l + 1)
        return maxString

S = Solution()

#Testcases
print(S.lengthOfLongestSubstring("abcabcbb")) #Expected = 3, Answer = 1
print(S.lengthOfLongestSubstring("bbbbb")) #Expected = 1, Answer = 1
print(S.lengthOfLongestSubstring("pwwkew")) #Expected = 3, Answer = 3