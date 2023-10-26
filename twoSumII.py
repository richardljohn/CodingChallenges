# Leetcode #167 - Two Sum II

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
            if currentSum > target: 
                r -= 1
            else: 
                return [l + 1, r + 1]
        
        return []