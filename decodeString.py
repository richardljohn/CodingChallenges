#Leetcode Challenge #394 - Decode String

class Solution:
    def decodeString(self, s: str) -> str:
        new_str = ""
        numbers = "0123456789"
        num = 0
        s = ""

        l, r = 0, 0

        while r < len(s): 
            if s[l] in numbers: 
                num = int(s[l])
                r = l + 1 
            if s[r] == "[":
                s += 1
                while s[r] != "]":
                    s += s[r]
                    r += 1
                new_str += s
                s = ""
                r += 1
                l = r 
        return new_str