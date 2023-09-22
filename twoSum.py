# Leetcode 1 - Two Sum (Done)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complimentMap = {}

        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in complimentMap:
                return [complimentMap[compliment], i]
            else:
                complimentMap[nums[i]] = i
        return []

        


s = Solution()

# Testcases
print(s.twoSum([2,7,11,15], 9)) # [0, 1]
print(s.twoSum([3,2,4], 6)) # [1, 2]
print(s.twoSum([3,3], 6)) # [0, 1]
print(s.twoSum([1, 2, 3, 4, 5, 6, 7, 8], 9))