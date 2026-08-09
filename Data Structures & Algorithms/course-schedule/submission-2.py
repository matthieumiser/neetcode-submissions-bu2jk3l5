from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        adj = {}
        for a, b in prerequisites:
            adj.setdefault(b, []).append(a)
            adj.setdefault(a, [])
        indeg = {n: 0 for n in adj}
        for n in adj:
            for nbr in adj[n]:
                indeg[nbr] += 1
        seen = 0
        q = deque(n for n in adj if indeg[n] == 0)
        while q:
            curr = q.popleft()
            seen += 1
            for i in adj[curr]:
                indeg[i] -= 1
                if indeg[i] == 0:
                    q.append(i)
        return seen == len(adj)