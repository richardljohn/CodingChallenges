# Leetcode # 11 - Container With Most Water

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # Brute Force
        # Does not work

        # maxWater = 0

        # for l in range(len(height)):
        #     for r in range(1 + l, len(height)):
        #         area = (r - l) * min(height[l], height[r])
        #         maxWater = max(maxWater, area)

        maxWater = 0
        l = 0
        r = len(height) - 1

        while l < r: 
            area = (r - l) * min(height[l], height[r])
            maxWater = max(area, maxWater)

            if height[l] < height[r]:
                l += 1
            else: 
                r -= 1

        return maxWater

S = Solution()

print(S.maxArea([1,8,6,2,5,4,8,3,7])) #49 Correct
print(S.maxArea([1,1])) #1 Correct