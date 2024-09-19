"""
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
the smallest in lexicographical order among all possible results.

Solution:
Time Complexity: O(N)
Space Complexity: O(N)

"""

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        stack = []
        visited = set()

        last_occur = {c: i for i, c in enumerate(s)}

        for i , c in enumerate(s):

            if c not in visited:
                while stack and ord(c) < ord(stack[-1]) and i < last_occur[stack[-1]]:
                    visited.discard(stack.pop())

                visited.add(c)
                stack.append(c)

        return ''.join(stack)
