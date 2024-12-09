# Leetcode #215 - Find Kth Largest

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]

S = Solution()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(S.findKthLargest(numbers, 2))