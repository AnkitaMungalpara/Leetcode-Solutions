"""
Given a string s, find the length of the longest substring without repeating characters.

Solution:
Time Complexity: O(N)
Space Complexity: O(Min(N,M))

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        i = 0
        letters = set()
        length = 0

        for j in range(len(s)):
            while s[j] in letters:
                letters.remove(s[i])
                i += 1

            letters.add(s[j])
            length = max(length, j-i+1)
        
        return length

