class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for i, x in enumerate(points):
            dist = x[0]**2 + x[1]**2
            heapq.heappush(max_heap, [-dist, -i, x])
            if len(max_heap) > k: heapq.heappop(max_heap)
        return [x[2] for x in max_heap]
            
            