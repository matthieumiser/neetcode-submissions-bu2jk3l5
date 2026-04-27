class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        hi, lo = max(piles), 1
        while hi >= lo:
            mid = (hi + lo) // 2
            if self.hoursToEat(piles, mid) <= h:
                hi = mid - 1
            elif self.hoursToEat(piles, mid) > h:
                lo = mid + 1
        if self.hoursToEat(piles, mid) > h:
            return mid + 1
        else:
            return mid
    
    def hoursToEat(self, piles, rate):
        hours = 0
        for i in piles:
            hours += -(i // -rate)
        return hours