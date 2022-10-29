# LeetCode Challenge #12 - Integer to Roman
# Convert Integers to Roman Numerals

class Solution:
    def intToRoman(self, num: int) -> str:
        romanList = [ 
        ["I", 1], ["IV", 4], ["V", 5], ["IX", 9], 
        ["X", 10], ["XL", 40], ["L", 50], ["XC", 90], 
        ["C", 100], ["CD", 400], ["D", 500], ["CM", 900], 
        ["M", 1000] ]

        res = ""

        for r, v in reversed(romanList): 
            if num // v:
                count = num // v
                res += (r * count)
                num = num % v
        return res