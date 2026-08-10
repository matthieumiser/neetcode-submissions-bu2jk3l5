class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {}
        for a, b in edges:
            graph.setdefault(a, []).append(b)
            graph.setdefault(b, []).append(a)
        for i in range(n):
            graph.setdefault(i, [])
        visited = set()
        def dfs(parent, node):
            if node in visited:
                return False
            visited.add(node)
            ret = True
            for i in graph[node]:
                if i != parent:
                    ret &= dfs(node, i)
            return ret
        return dfs(-1, 0) and len(visited) == n