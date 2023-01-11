import math

def twoSumLess(nums, k):
    maxNum = (float("-inf"))
    for i in range(0, len(nums) - 1, 1):
        for j in range(1, len(nums)-1, 1): 
            sum = nums[i] + nums[j]
            if sum < k and sum > maxNum: 
                maxNum = sum
    return maxNum if maxNum >= 0 else -1

# Test Case 1: Will output 58
print(twoSumLess([34, 23, 1, 24, 75, 33, 54, 8], 60))

# Test Case 2: Will output -1
print(twoSumLess([10, 20, 30], 15))