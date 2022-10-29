def isAnagrams(s1, s2):
    if len(s1) != len(s2):
        return False 
    
    mapOne, mapTwo = {}, {}

    for i in range(len(s1)):
        mapOne[s1[i]] = 1 + mapOne.get(s1[i], 0)
        mapTwo[s2[i]] = 1 + mapTwo.get(s2[i], 0)

    for m in mapOne:
        if mapOne[m] != mapTwo.get(m, 0):
            return False

    return True