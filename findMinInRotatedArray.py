# LeetCode #153 - Find Minimum in Rotated Array

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l, r = 0, len(nums) - 1 
        


        while l < r:
            if nums[l] > nums[r]:
                