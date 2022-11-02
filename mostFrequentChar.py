def most_frequent_char(s):
    if len(s) < 1:
        return ""
    if len(s) == 1: 
        return s

    charMap = {}
    for i in range(len(s)):
        charMap[s[i]] = 1 + charMap.get(s[i], 0)
    return max(charMap, key=charMap.get)

print(most_frequent_char("Alfonso"))