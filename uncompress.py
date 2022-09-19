def uncompress(s): 
    numbers = "0123456789"
    new_str = ""
    # new_str = []
    i, j = 0, 0


    while j < len(s):
        if s[j] in numbers:
            j += 1
        else: 
            num = int(s[i:j])
            new_str += s[j] * num
            # new_str.append(s[j] * num)
            j += 1
            i = j
    # return new_str
    return ''.join(new_str)


print(uncompress("2c3a1t"))