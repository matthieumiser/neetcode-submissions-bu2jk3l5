class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        for u, v in prerequisites:
            graph.setdefault(v, []).append(u)
            graph.setdefault(u, [])
        for n in range(numCourses):
            graph.setdefault(n, [])

        indeg = {n: 0 for n in graph}
        for n in graph:
            for nbr in graph[n]:
                indeg[nbr] += 1
        
        q = deque(i for i in graph if indeg[i] == 0)
        print(q)
        ordering = []
        seen = set()
        while q:
            cur = q.popleft()
            seen.add(cur)
            ordering.append(cur)
            for nbr in graph[cur]:
                indeg[nbr] -= 1
                if indeg[nbr] == 0:
                    q.append(nbr)
        return ordering if len(seen) == numCourses else []