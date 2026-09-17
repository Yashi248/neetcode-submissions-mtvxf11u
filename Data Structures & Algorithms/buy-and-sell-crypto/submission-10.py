class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l,r = 0,1

        for r in range(1,len(prices)):
            if prices[l]<prices[r]:
                maxP = max(maxP, prices[r]-prices[l])
            else:
                l=r
            #r+=1
        return maxP