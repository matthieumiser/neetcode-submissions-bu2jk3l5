class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        curr = 0
        max_profit = 0
        for i, x in enumerate(prices):
            if x > prices[curr]:
                curr = i
            if prices[curr] - prices[start] > max_profit:
                max_profit = prices[curr] - prices[start]
            if x < prices[start]:
                start = i
                curr = i
            
        return max_profit