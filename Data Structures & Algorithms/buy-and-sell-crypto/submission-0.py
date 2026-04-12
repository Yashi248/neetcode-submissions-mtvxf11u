class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1,len(prices)):
            l = i-1
            while (l > -1) and (prices[l] < prices[i]):
                profit = prices[i] - prices[l]
                max_profit = max(profit, max_profit)
                l-=1
        return max_profit
