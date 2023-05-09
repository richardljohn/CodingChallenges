# LeetCode #153 - Find Minimum in Rotated Array (Done)

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        l, r = 0, len(nums) - 1 
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break 

            m = (l + r) // 2 
            res = min(res, nums[m])
            if nums[m] >= nums[l]: 
                l = m + 1 
            else: 
                r = m - 1 
        return res 


#Test Cases (Passed)
print(findMin([3,4,5,1,2])) #1
print(findMin([4,5,6,7,0,1,2])) #0
print(findMin([11,13,15,17])) #11