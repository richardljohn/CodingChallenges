# Leetcode #42 - Trapping Rain Water

class Solution:
    def trap(self, height: List[int]) -> int:

        totalWater = 0
        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]

        while l < r: 
            if maxLeft < maxRight: 
                water = maxLeft - height[l]
                totalWater += water if water > 0 else 0
                maxLeft = max(maxLeft, height[l])
                l += 1
            else: 
                water = maxRight - height[r]
                totalWater += water if water > 0 else 0
                maxRight = max(maxRight, height[r])
                r -= 1
                
        return totalWater

S = Solution()

# Testcases
print(S.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(S.trap([4,2,0,3,2,5]))