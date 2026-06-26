class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        l,r=0,1
        while r < len(prices):
            profit=prices[r]-prices[l]
            if prices[r] < prices[l]:
                l=r
            maxprofit=max(maxprofit,profit)
            r+=1
        return maxprofit
        