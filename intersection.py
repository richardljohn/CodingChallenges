def intersection(a, b):
    if a == [] or b == []:
        return []

    inter = []
    c = set()
    for i in range(len(a)):
        c.add(a[i])
    for i in range(len(b)):
        if b[i] in c: 
            inter.append(b[i])
    return inter

print(intersection([1, 4, 5, 6, 7], [1, 2, 3]))