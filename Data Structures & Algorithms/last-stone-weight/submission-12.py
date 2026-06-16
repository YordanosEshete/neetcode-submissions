import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i, x in enumerate(stones):
            stones[i] = -x
        
        heapq.heapify(stones)

        while len(stones) >= 2:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)

            if x > y:
                heapq.heappush(stones, -(x-y))
        
        if len(stones) == 0:
            return 0
        else:
            return -stones[0]


        
        
        
        