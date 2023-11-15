# LeetCode # 128 - Longest Consecutive Sequence

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        numSet = set(nums)
        currSequence = 0
        longest = 0

        for n in numSet:
            if (n - 1) in numSet:
                currSequence += 1 
                while (n + length) in numSet:
                    currSequence += 1
                longest = max(currSequence, longest)
        return longest