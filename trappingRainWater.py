# Leetcode #42 - Trapping Rain Water

class Solution:
    def trap(self, height: List[int]) -> int:

        water = 0
        l, r = 0, len(height) - 1
        maxLeft, maxRight = 0, 0 

        