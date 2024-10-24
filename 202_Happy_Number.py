"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Solution:
Time Complexity: O(1)
Space Complexity: O(1)

"""

class Solution:
    def isHappy(self, n: int) -> bool:

        def get_next(num):
            total = 0
            while num > 0:
                num, digit = divmod(num, 10)
                total += digit ** 2
            return total

        while n != 1 and n != 4:
            n = get_next(n)

        return n == 1
      
