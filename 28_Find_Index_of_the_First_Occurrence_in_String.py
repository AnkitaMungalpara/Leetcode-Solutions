"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # Method 1:
        ## Time Complexity: O(N+M)
        ## Space Complexity: O(1)
        
        return haystack.find(needle)

        # Method 2:
        ## Time Complexity: O(N+M)
        ## Space Complexity: O(1)

        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
