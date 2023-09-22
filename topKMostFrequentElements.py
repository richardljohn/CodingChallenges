class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        numsMap = {}
        numsList = []

        for num in nums:
            numsMap[num] = 1 + numsMap.get(num, 0)
        
        numsMap = sorted(numsMap, key=numsMap.get, reverse=True)

        for i in range(k):
            numsList.append(list(numsMap[i]))
        
        return numsList