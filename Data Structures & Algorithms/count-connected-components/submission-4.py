class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        for u, v in edges:
            graph.setdefault(u, []).append(v)
            graph.setdefault(v, []).append(u)
        for i in range(n):
            graph.setdefault(i, [])
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nbr in graph[node]:
                dfs(nbr)
        sets = 0
        print(graph)
        for i in graph:
            if len(visited) == n: break
            if i not in visited: 
                dfs(i)
                sets += 1
                print(i, visited)
        return sets