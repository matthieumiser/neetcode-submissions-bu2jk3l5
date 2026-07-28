class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        counter = []
        for i, x in enumerate(points):
            distances.append(math.sqrt(x[0]**2 + x[1]**2))
            counter.append(i)
        zipped = list(zip(distances, counter, points))
        heapq.heapify(zipped)

        out = []
        for i in range(k):
            out.append(heapq.heappop(zipped)[2])
        return out
            
            