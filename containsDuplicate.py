# LeetCode #217 - Contains Duplicate

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        duplicate = set() 

        for i in range(len(nums)):
            if nums[i] in duplicate:
                return True
            duplicate.add(nums[i])
        return False

print(Solution.containsDuplicate([1, 2, 3,]))