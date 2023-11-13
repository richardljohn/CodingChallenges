# Leetcode #167 - Two Sum II (Done)

# A bit of a weird one with the output. You treat it as a regular array, but you must return the 
# indices as one more than their actual index. For example, if your solution has the indices
# 0 and 1, you must return 1 and 2 as your answer.

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(numbers) - 1

        while l < r: 
            currentSum = numbers[l] + numbers[r]

            if currentSum < target: 
                l += 1

            elif currentSum > target: 
                r -= 1

            else: 
                return [l + 1, r + 1]
        
        return []

s = Solution()
# Example 1:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
print(s.twoSum([2, 7, 11, 15], 9))

# Example 2:
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
print(s.twoSum([2, 3, 4], 6))

# Example 3:
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
print(s.twoSum([-1, 0], -1))

# All examples passed. Good work on this Leetcode. Onto the next.