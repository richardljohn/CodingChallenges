def missingRanges(nums, lower, upper): 
    res = []
    if lower - upper == 0: 
        return [lower]
    if len(nums) == 0: 
        res.append(str(lower) + "->" + str(upper))
        return res
    

    start, end = 0, 1
    while start < len(nums) and end < len(nums):
        if nums[start] + 1 == nums[end]: 
            firstNum = nums[start]
            start += 1
            end += 1
            while nums[start] + 1 == nums[end]:
                start += 1
                end += 1
            res.append(str(end))
            start += 1 
            end += 1
            
            if(nums[end] + 1 != nums[end+1]):
                res.append()

    return res 

print(missingRanges([], 0, 100))
