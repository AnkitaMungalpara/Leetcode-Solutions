"""
Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

Solution:
Time Complexity: O(N)
Space Complexity: O(N)

"""

class Solution:
    def smallestSubsequence(self, s: str) -> str:

        stack = []
        visited = set()

        last_occur = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):

            if c not in visited:
                while stack and ord(c) < ord(stack[-1]) and i < last_occur[stack[-1]]:
                    visited.discard(stack.pop())
                
                visited.add(c)
                stack.append(c)
        
        return ''.join(stack)
