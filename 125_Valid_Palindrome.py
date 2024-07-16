"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Solution:
Time Complexity: O(N)
Space Complexity: O(N)

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([ch.lower() for ch in s if ch.isalnum()])

        for i in range(len(s)):
            if s[i] == s[-(i+1)]:
                continue
            else:
                return False

        return True
