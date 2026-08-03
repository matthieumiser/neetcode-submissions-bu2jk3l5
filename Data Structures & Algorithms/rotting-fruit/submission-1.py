class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        def visit(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return
            if grid[i][j] == 0 or (i, j) in visited or grid[i][j] == 2:
                return
            q.append((i, j))
            visited.add((i, j))
        fruits = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    q.append((i, j))
                    visited.add((i, j))
                    fruits += 1
                elif grid[i][j] == 1:
                    fruits += 1
        mins = -1
        while q:
            print(visited)
            for i in range(len(q)):
                fruit = q.popleft()
                visit(fruit[0], fruit[1] - 1)
                visit(fruit[0], fruit[1] + 1)
                visit(fruit[0] - 1, fruit[1])
                visit(fruit[0] + 1, fruit[1])
            mins += 1
        if mins < 0: mins = 0
        if len(visited) != fruits: mins = -1 
        return mins
