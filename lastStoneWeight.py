# Leetcode #1046 - Last Stone Weight

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = abs(heapq.heappop(stones))
            second = abs(heapq.heappop(stones))

            if first > second:
                heapq.heappush(stones, -1*(first-second))
        
        if not stones:
            return 0 
        return abs(stones[0])