# LeetCode #53 - Maximum Subarray

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxSub = nums[0]
        currSum = 0

        for num in nums:
            if currSum < 0:
                currSum = 0
            currSum += num
            maxSub = max(maxSub, currSum)
        return maxSub

s = Solution()

# Test Cases
print(s.maxSubArray(s, [-2,1,-3,4,-1,2,1,-5,4]))
print(s.maxSubArray(s, [1]))
print(s.maxSubarray(s, [5,4,-1,7,8]))