class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        numsMap = {}

        for num in nums:
            numsMap[num] = 1 + numsMap.get(num, 0)
        
        numsList = sorted(numsMap, key=numsMap.get, reverse=True)
        
        return numsList[0:k]

s = Solution()

print(s.topKFrequent([1, 1, 1, 2, 2, 3, 4], 2))