class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        def search(i, j):
            if i < 0 or i >= len(grid):
                return
            elif j < 0 or j >= len(grid[0]):
                return
            elif grid[i][j] == "0":
                return
            grid[i][j] = "0"

            search(i + 1, j)
            search(i, j + 1)
            search(i - 1, j)
            search(i, j - 1)
            
        for i, x in enumerate(grid):
            for j, y in enumerate(x):
                if y == "1":
                    islands += 1
                    search(i, j)
        return islands
        