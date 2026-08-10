class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {}
        for a, b in edges:
            graph.setdefault(a, []).append(b)
            graph.setdefault(b, []).append(a)
        for i in range(n):
            graph.setdefault(i, [])
        q = [(0, None)]
        visited = set()
        while q:
            curr, parent = q.pop()
            visited.add(curr)
            for i in graph[curr]:
                stack_itm = (i, curr)
                if i in visited and parent != i:
                    return False
                if i not in visited: q.append(stack_itm)
        if len(visited) != n:
            return False
        return True