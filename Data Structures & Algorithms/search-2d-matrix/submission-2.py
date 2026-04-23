class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = 0, (len(matrix) * len(matrix[0])) - 1
        while lo <= hi:
            mid = (hi + lo) // 2
            print(lo, mid, hi)
            mid_val = self.getIndex(matrix, mid)
            if mid_val == target:
                return True
            elif mid_val < target:
                lo = mid + 1
            elif mid_val > target:
                hi = mid - 1
        return False
        
    def getIndex(self, matrix, idx):
        y = idx // len(matrix[0])
        x = idx - (y * len(matrix[0]))
        print(y, x)
        return matrix[y][x]
