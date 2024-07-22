"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.

Solution:
Time Complexity: O(N)
Space Complexity: O(N)

"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        mapping = defaultdict(lambda: 0)
        revised_s = list()

        for i in range(len(s)):
            if s[i] not in mapping and t[i] not in mapping.values():
                mapping[s[i]] = t[i]
            revised_s.append(str(mapping[s[i]]))

        return True if ''.join(revised_s) == t else False
