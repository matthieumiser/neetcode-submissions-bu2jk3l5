class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        w = len(matrix[0])
        h = len(matrix)

        i = 0
        j = 0

        out = []
        direction = "r"

        def get_direction(v, d, i, j):
            if d == "r" and j >= w - 1:
                return "d"
            elif d == "d" and i >= h - 1:
                return "l"
            elif d == "l" and j <= 0:
                return "u"
            elif d == "u" and i <= 0:
                return "r"
            
            elif d == "r" and v[i][j + 1] == None:
                return "d"
            elif d == "d" and v[i + 1][j] == None:
                return "l"
            elif d == "l" and v[i][j - 1] == None:
                return "u"
            elif d == "u" and v[i - 1][j] == None:
                return "r"
            return direction
        # i vert j horiz
        for _ in range(w * h):
            out.append(matrix[i][j])
            matrix[i][j] = None
            direction = get_direction(matrix, direction, i, j)
            if direction == "r":
                j += 1
            elif direction == "d":
                i += 1
            elif direction == "l":
                j -= 1
            elif direction == "u":
                i -= 1
        return out