def pairSum(numbers, targetSum):
    if len(numbers) < 1:
        return 

    numMap = {}
    for i, n in enumerate(numbers):
        diff = targetSum - n
        if diff in numMap:
            return (numMap[diff], i)
        else: 
            numMap[n] = i
    return

print(pairSum([1, 2, 3, 4, 5], 3))