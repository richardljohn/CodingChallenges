# Random Question: 

def reverseStrings(s): 
    newStr = ""
    stack = []
    l, r = 0, 0

    while l < len(s) and r < len(s): 
        if s[r] != '.': 
            r += 1
        else:
            stack.append(s[l:r])
            l = r + 1
            r = l
        if r == len(s) - 1:
            stack.append(s[l:r+1])
        
    
    while stack: 
        newStr += stack.pop()
        if len(stack) != 0:
            newStr += "."

    return newStr

print(reverseStrings("i.like.this.program.very.much"))