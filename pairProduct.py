def pairProduct(numbers, targetProduct):
    if len(numbers) < 1:
        return 
    
    numMap = {}
    for i, n in enumerate(numbers):
        quot = targetProduct / n
        if quot in numMap:
            return (numMap[quot], i)
        else: 
            numMap[n] = i
    return 

print(pairProduct([1, 2, 3, 4, 5], 8))