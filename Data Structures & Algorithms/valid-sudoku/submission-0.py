from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        gridmap = defaultdict(set)
        ymap = defaultdict(set)
        xmap = defaultdict(set)
        for y, row in enumerate(board):
            for x, val in enumerate(row):
                if val != '.':
                    if not (0 < int(val) < 10):
                        return False
                    if val in xmap[x]:
                        return False
                    if val in ymap[y]:
                        return False
                    if val in gridmap[self.getGridSquare(x,y)]:
                        return False
                    xmap[x].add(val)
                    ymap[y].add(val)
                    gridmap[self.getGridSquare(x,y)].add(val)

        return True


    def getGridSquare(self, x, y):
        return tuple([x // 3, y // 3])
        