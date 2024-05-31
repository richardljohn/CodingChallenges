# Leetcode # 1304 - Find N Unique Integers Which Sum to Zero

class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []

        if n % 2 == 1 or n == 1: 
            res.append(0)
            for i in range(1, n // 2 + 1):
                res.append(i)
                res.append((i * -1))
        else: 
            for i in range(1, n // 2 + 1):
                res.append(i)
                res.append(i * -1)
        return res

S = Solution()

print(S.sumZero(5))