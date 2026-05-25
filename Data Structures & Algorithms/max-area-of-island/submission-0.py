class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def search(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return
            elif grid[i][j] == 0:
                return

            search.calls += 1
            grid[i][j] = 0

            search(i + 1, j)
            search(i - 1, j)
            search(i, j + 1)
            search(i, j - 1)
            
        m = 0 
        for i, x in enumerate(grid):
            for j, y in enumerate(x):
                if y == 1:
                    search.calls = 0
                    search(i, j)
                    m = max(search.calls, m)
        return m