# Leetcode #121 - Best Time to Buy and Sell Stock

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else: 
                l = r
            r += 1
        
        return maxProfit

S = Solution()

#Testcases
print(S.maxProfit([7,1,5,3,6,4]))
print(S.maxProfit([7,6,4,3,1]))