# Leetcode #704 - Binary Search (Done).

# Libraries
from ast import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1

S = Solution()

# Test Cases
# Input: nums = [-1,0,3,5,9,12], target = 9
# Expected Output: 4
print(S.search([-1,0,3,5,9,12], 9))
# Output: 4

# Input: nums = [-1,0,3,5,9,12], target = 2
# Expected Output: -1
print(S.search([-1,0,3,5,9,12], 2))
# Output: -1