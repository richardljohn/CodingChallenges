def fiveSort(nums):
    if len(nums) == 0:
        return

    i = 0
    curr = len(nums) - 1
    while i < curr:
        if nums[i] != 5:
            i += 1
        else: 
            nums[i], nums[curr] = nums[curr], nums[i]
            curr -= 1
            i += 1
        # if nums[curr] == 5: 
        #     curr -= 1
        # elif nums[i] == 5: 
        #     nums[i], nums[curr] = nums[curr], nums[i]
        #     i += 1
        # else: 
        #     i += 1
        
    return nums

print(fiveSort([5, 5, 1, 2, 3]))

# Have a pointer at the end of the array
# For loop. 
# If you encounter a 5:
# Swap current place with pointer. 
# move pointer up by 1.