# LeetCode #152 - Maximum Product

def maxProduct(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = max(nums)
        currMin, currMax = 1, 1
        for num in nums: 
            if num == 0: 
                currMin, currMax = 1, 1
                continue

            tmp = currMax * num
            currMax = max(num * currMax, num * currMin, num)
            currMin = min(tmp, num * currMin, num)
            res = max(res, currMax)
        return res

#Test Cases Passed
print(maxProduct([2,3,-2,4])) #6
print(maxProduct([-2,0,-1])) #0