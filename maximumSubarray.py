# LeetCode #53 - Maximum Subarray

def maxSubArray(nums):
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

# Test Cases
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([1]))
print(maxSubArray([5,4,-1,7,8]))