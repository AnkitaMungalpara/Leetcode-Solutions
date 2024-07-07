"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

Solution:
Time Complexity: O(N)
Space Complexity: O(1)

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxProfit += (prices[i] - prices[i-1])
                
        return maxProfit