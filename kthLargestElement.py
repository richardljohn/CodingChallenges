# Random Question - Kth Largest Element

def findK(k, n, arr):
    found = []
    if n == 0 or k > n: 
        return -1
    for i in range(n):
        if k > i: 
            found.append(-1)
        else: 
            num = arr[k-i-1]
            found.append(num)
    return found

print(findK(4, 6, [1, 2, 3, 4, 5, 6]))