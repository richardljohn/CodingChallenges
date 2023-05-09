# Leetcode 1 - Two Sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = 1
        count = 0 

        while l < len(nums):
            while r < len(nums):
                if nums[l] + nums[r] == target:
                    return True
                r += 1 
            l += 1