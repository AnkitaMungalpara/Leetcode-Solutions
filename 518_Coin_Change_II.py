"""

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

Solution:
Time Complexity: O(N * Amount)
Space Complexity: O(Amount)

"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins:
            for a in range(c, amount+1):
                dp[a] += dp[a-c]
                
                 
        return dp[amount]

  
