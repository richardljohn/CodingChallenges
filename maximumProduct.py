# LeetCode #152 - Maximum Product

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxProd = nums[0]
        currProd = 1


        for num in nums:
            if currProd < 0 and num > 0:
                currProd = 1
            currProd *= num
            maxProd = max(maxProd, currProd)
        
        return maxProd

