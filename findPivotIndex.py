#Leetcode Challenge #724 - Find Pivot Index 

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)

        leftSum = 0 
        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum
            if rightSum == leftSum:
                return i
            else: 
                leftSum += nums[i]
        return -1