# Leetcode #1822 - Sign of the Product of an Array

class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        product = 1 
        for num in nums: 
            if num == 0: 
                return 0
            elif num > 0: 
                product = product * 1
            elif num < 0: 
                product = product * -1
        return product

S = Solution()
print(S.arraySign([-1,-2,-3,-4,3,2,1]))