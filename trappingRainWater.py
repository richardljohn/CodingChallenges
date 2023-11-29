# Leetcode #42 - Trapping Rain Water

class Solution:
    def trap(self, height: List[int]) -> int:

        water = 0
        l, r = 0, len(height) - 1
        maxLeft, maxRight = 0, 0 

        while l < r: 
            maxLeft = max(maxLeft, height[l])
            maxRight = max(maxRight, height[r])

            if maxLeft < maxRight: 
                l += 1
                total = maxLeft - height[l]
                water += total if total > 0 else 0
            else:
                r -= 1