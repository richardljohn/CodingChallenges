class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        start, curr, end = nums[0], nums[0], None
        res = []
        for n in nums[1:]:
            curr += 1
            if n == curr: 
                end = n 
            else:
                if not end: 
                    res.append(str(start))
                else: 
                    res.append(str(start) + "->" + str(end))
                start = n 
                end = n 
                end = None
            if not end: 
                res.append(str(start))
            else: 
                res.append(str(start)+"->"+str(end))
            return res