# LeetCode # 128 - Longest Consecutive Sequence

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in numSet:
                currSequence = 0
                while (n + currSequence) in numSet:
                    currSequence += 1
                longest = max(currSequence, longest)

        return longest