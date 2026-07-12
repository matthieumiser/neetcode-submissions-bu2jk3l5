class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = abs(heapq.heappop(stones))
            y = abs(heapq.heappop(stones))
            if x == y:
                continue
            else:
                heapq.heappush(stones, -max(x, y) - (-min(x, y)))
        return abs(stones[0]) if len(stones) > 0 else 0
            