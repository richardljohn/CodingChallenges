# Leetcode # 11 - Container With Most Water

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxWater = 0

        # Brute Force

        for l in range(len(height)):
            for r in range(1 + l, len(height)):
                area = (r - l) * min(height[l], height[r])
                maxWater = max(maxWater, area)

        return maxWater

S = Solution()

print(S.maxArea([1,8,6,2,5,4,8,3,7]))
print(S.maxArea([1,1]))