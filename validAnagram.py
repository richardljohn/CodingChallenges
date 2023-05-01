# LeetCode #242 - Valid Anagram

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): 
            return False

        i = 0
        sMap, tMap = {}, {}
        while i < len(s):
            sMap[s[i]] = 1 + sMap.get(s[i], 0)
            tMap[t[i]] = 1 + tMap.get(t[i], 0)
            i += 1 
        
        for c in sMap:
            if sMap[c] != tMap.get(c, 0):
                return False
        
        return True

# Test Cases 
s = Solution()
print(s.isAnagram("anagram", "nagamar")) #True
print(s.isAnagram("anagramm", "nagamar")) #True
