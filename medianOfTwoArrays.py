class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i = 0
        while i < len(nums2):
            if nums2[i] not in nums1: 
                nums1.append(nums2[i])

        nums1.sort()
        if len(nums1) % 2 == 0: 
            return nums1[len(nums1)/2]
        else: 
            val = nums1[len(nums1)/2] + nums1[1 + len(nums1)/2]
            return val 