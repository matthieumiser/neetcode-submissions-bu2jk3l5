class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def is_out(i, j):
            return i < 0 or j < 0 or i >= len(board) or j >= len(board[0])
        visited = set()
        def dfs(i, j):
            if is_out(i, j):
                return
            if board[i][j] == 'X':
                return
            if (i, j) in visited:
                return
            visited.add((i, j)) 
            a = dfs(i + 1, j)
            b = dfs(i - 1, j)
            c = dfs(i, j + 1)
            d = dfs(i, j - 1)
        
        for i in range(len(board)):
            dfs(i, 0)
            dfs(i, len(board[0]) - 1)
        for j in range(len(board[0])):
            dfs(0, j)
            dfs(len(board) - 1, j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i, j) not in visited:
                    board[i][j] = 'X'