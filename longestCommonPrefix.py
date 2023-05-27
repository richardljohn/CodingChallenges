# LeetCode #14 - Longest Common Prefix

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        res = ""
        
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]

        return res

# Test Cases 

S = Solution()
print(S.longestCommonPrefix(["flower","flow","flight"]))
print(S.longestCommonPrefix(["dog","racecar","car"]))
print(S.longestCommonPrefix(["car", "cat", "catman", "catmania"]))