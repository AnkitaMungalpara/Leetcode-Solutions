"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:

Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Solution:
Time Complexity: O(M*N)
Space Complexity: O(M*N)

"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[m - 1][n - 1] = 1

        for row in range(m-1, -1, -1):
            for col in range(n-1, -1, -1):
                if row + 1 < m:
                    dp[row][col] += dp[row + 1][col]
                if col + 1 < n:
                    dp[row][col] += dp[row][col + 1]

        return dp[0][0]
    
      
