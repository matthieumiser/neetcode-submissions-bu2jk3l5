class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [None] * len(cost)
        def recurse(i):
            if i >= len(cost):
                return 0
            elif cache[i]:
                return cache[i]
            cache[i] = min(recurse(i + 1), recurse(i + 2)) + cost[i]
            return cache[i]
        return min(recurse(0), recurse(1))