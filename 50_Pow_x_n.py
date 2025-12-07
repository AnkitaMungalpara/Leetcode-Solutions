"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000

Explanation: 2-2 = 1/22 = 1/4 = 0.25


Solution:
Time Complexity: O(logN)
Space Complexity: O(logN)

"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def dfs(x, n):

            if x == 0:
                return 0

            if n == 0:
                return 1

            res = dfs(x, n // 2)
            res = res * res

            res = x * res if n % 2 else res
            return res

        
        out = dfs(x, abs(n))

        return out if n >= 0 else 1/out
            
      
