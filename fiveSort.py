def fiveSort(nums):
    if len(nums) == 0:
        return

    i = 0
    curr = len(nums) - 1
    while i < curr:
        # if nums[i] != 5:
        #     i += 1
        # else: 
        #     nums[i], nums[curr] = nums[curr], nums[i]
        #     curr -= 1
        #     i += 1
        if nums[curr] == 5: 
            curr -= 1
        elif nums[i] == 5: 
            nums[i], nums[curr] = nums[curr], nums[i]
            i += 1
        else: 
            i += 1
        
    return nums

print(fiveSort([5, 5, 1, 2, 3]))



# Pseudocode.
# Have a pointer at the end of the array
# For loop. 
# If you encounter a 5:
# Swap current place with pointer. 
# move pointer up by 1.
# when loop reaches same spot as the pointer, end the loop.
# else, continue.

# Explanation: 
# There are two pointers. One at the start and one at the end. 
# With each iteration of the loop, we will do a few checks.
# Check to see if the end pointer is at a 5. If it does:
# We move the end pointer up by one space.
# If it is not: 
# We check the pointer at the start and see if it is at a 5. 
# If it is: 
# We swap the left pointer value with the one at the end. 
# Afterwards we move the left pointer up one space.
# If neither condition is true, we simply move the left pointer up one. 
# This will resume until the left pointer is either at the same spot as the right pointer, or past it.