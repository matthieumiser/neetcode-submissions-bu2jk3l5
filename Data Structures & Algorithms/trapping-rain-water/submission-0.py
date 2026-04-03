class Solution:
    def trap(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height) - 1
        sealevel = 0
        watercount = 0
        while p1 < p2:
            currmin = min(height[p1], height[p2])
            sealevel = currmin if currmin > sealevel else sealevel
            
            if height[p1] > height[p2]:
                watercount += sealevel - height[p2]
                p2 -= 1
            else:
                watercount += sealevel - height[p1]
                p1 += 1
        return watercount
            