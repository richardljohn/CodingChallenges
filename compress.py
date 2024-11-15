def compress(s): 
    s += "!"
    new_str = ""
    i, j = 0, 0

    while j < len(s):
        if s[i] == s[j]: 
            j += 1
        else: 
            num = j - i
            if num == 1:
                new_str += s[i]
            else: 
                new_str += (str(num))
                new_str += s[i]
            i = j

    return new_str

print(compress("aaattttt"))
print(compress("cccaaaattttt"))
print(compress("bbbbbbaaattttt"))
print(compress("adaattttt"))