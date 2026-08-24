class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i,j=0,1
        n=len(prices)
        maxi=0
        while(j<=n-1):
            if prices[j]-prices[i]<0:
                i=j
                j+=1
            else:
                maxi=max(maxi, prices[j]-prices[i])
                j+=1
        return maxi

        