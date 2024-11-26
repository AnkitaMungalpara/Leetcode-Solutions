"""
You are given two positive integers n and k. A factor of an integer n is defined as an integer i where n % i == 0.

Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.

Solution:
Time Complexity: O(N)
Space Complexity: O(1)

"""

class Solution:
    def kthFactor(self, n: int, k: int) -> int:

        factor = 0
        for i in range(1, n+1):
            if n % i == 0:
                factor += 1
            if factor == k:
                return i
        return -1
        
