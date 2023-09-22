from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        mp = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            mp[sorted_word].append(word)
        
        return mp.values()

s = Solution()


print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))