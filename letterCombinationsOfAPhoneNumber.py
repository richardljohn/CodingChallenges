# Leetcode #17 - Letter Combinations of a Phone Number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        

        res = []

        digitsToChars = { 
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return

            for c in digitsToChars[digits[i]]:
                backtrack(i + 1, curStr +  c)
            
        if digits: 
            backtrack(0, "")