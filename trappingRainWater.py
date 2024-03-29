# Leetcode #42 - Trapping Rain Water (Done)

class Solution:
    def trap(self, height: list[int]) -> int:

        totalWater = 0
        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]

        while l < r: 
            if maxLeft < maxRight: 
                l += 1
                water = maxLeft - height[l]
                totalWater += water if water > 0 else 0
                maxLeft = max(maxLeft, height[l])
                
            else:
                r -= 1
                water = maxRight - height[r]
                totalWater += water if water > 0 else 0
                maxRight = max(maxRight, height[r])
                
        return totalWater

S = Solution()

# Testcases
print(S.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # Expected Answer = 6, Answer = 6
print(S.trap([4,2,0,3,2,5])) # Expected Answer = 9, Answer = 9
# Done