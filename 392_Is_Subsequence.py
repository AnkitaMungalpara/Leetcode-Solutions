"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Solution:
Time Complexity: O(N)
Space Complexity: O(1)

"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i = 0
        if len(s) > 0:
            for k in range(len(t)):
                if s[i] == t[k]:
                    i += 1
                    if i == len(s):
                        return True 
            return False
        else:
            return True
