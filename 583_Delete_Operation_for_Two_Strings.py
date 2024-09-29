"""
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

Solution:
Time Complexity: O(M * N)
Space Complexity: O(M * N)

"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n, m = len(word1), len(word2)

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for c in range(n+1):
            dp[0][c] = c
        
        for r in range(m+1):
            dp[r][0] = r

        for r in range(1, m+1):
            for c in range(1, n+1):
                if word1[c-1] == word2[r-1]:
                    dp[r][c] = dp[r-1][c-1]
                else:
                    dp[r][c] = min(dp[r-1][c], dp[r][c-1]) + 1

        return dp[-1][-1]
