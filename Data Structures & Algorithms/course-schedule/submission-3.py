from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for a, b in prerequisites:
            graph.setdefault(b, []).append(a)
            graph.setdefault(a, [])
        indeg = {n: 0 for n in graph}
        for n in graph:
            for nbr in graph[n]:
                indeg[nbr] += 1
        q = deque(n for n in graph if indeg[n] == 0)
        seen = 0
        while q:
            curr = q.popleft()
            seen += 1
            for nbr in graph[curr]:
                indeg[nbr] -= 1
                if indeg[nbr] == 0: q.append(nbr)
        return seen == len(graph)
