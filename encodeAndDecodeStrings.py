# Leetcode 271 - Encode and Decode Strings

class Solution:

    def encode(self, strs: list[str]) -> str:

        newStr = ""

        for s in strs: 
            newStr += str(len(s)) + "#" + s
        return newStr


    def decode(self, s: str) -> list[str]:
        
        decodedStrs, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            decodedStrs.append(s[j + 1: j + 1 + length])
            i = j + 1 + length

        return decodedStrs

strings = ["I", "am", "Batman"]

S = Solution()
strings = S.encode(strings)
print(S.decode(strings))