# LeetCode # 128 - Longest Consecutive Sequence

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in numSet:
                currSequence = 0
                while (n + currSequence) in numSet:
                    currSequence += 1
                longest = max(currSequence, longest)

        return longest

S = Solution()

# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
print(S.longestConsecutive([100, 4, 200, 1, 3, 2]))

# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
print(S.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))

