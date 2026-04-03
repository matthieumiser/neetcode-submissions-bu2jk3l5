class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        p1 = 0
        p2 = len(heights) - 1
        while p1 < p2:
            area = (p2 - p1) * min(heights[p2], heights[p1])
            if area > max_area:
                max_area = area
            if heights[p1] > heights[p2]:
                p2 -= 1
            else:
                p1 += 1
        return max_area