from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def is_in_bounds(coords):
            i = coords[0]
            j = coords[1]
            if i < 0 or j < 0:
                return False
            if i >= len(grid) or j >= len(grid[0]):
                return False
            return True

        queue = deque()
        inf = 2147483647
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j, grid[i][j]))
        while queue:
            curr = queue.popleft()
            if (curr[0], curr[1]) not in visited and is_in_bounds(curr) and grid[curr[0]][curr[1]] != -1:
                # visit
                currval = grid[curr[0]][curr[1]]
                rootval = curr[2]
                if currval == inf:
                    grid[curr[0]][curr[1]] = rootval + 1
                    currval = grid[curr[0]][curr[1]]
                visited.add((curr[0], curr[1]))
                # left
                queue.append((curr[0], curr[1] - 1, currval))
                # rightcurrval
                queue.append((curr[0], curr[1] + 1, currval))
                # upcurrval
                queue.append((curr[0] - 1, curr[1], currval))
                # downcurrval
                queue.append((curr[0] + 1, curr[1], currval))



