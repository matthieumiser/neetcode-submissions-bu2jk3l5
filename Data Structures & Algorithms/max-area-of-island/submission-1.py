class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def search(i, j, calls=0):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return calls
            elif grid[i][j] == 0:
                return calls

            calls += 1
            grid[i][j] = 0

            calls = search(i + 1, j, calls)
            calls = search(i - 1, j, calls)
            calls = search(i, j + 1, calls)
            calls = search(i, j - 1, calls)
            
            return calls
            
        m = 0 
        for i, x in enumerate(grid):
            for j, y in enumerate(x):
                if y == 1:
                    m = max(search(i, j), m)
        return m