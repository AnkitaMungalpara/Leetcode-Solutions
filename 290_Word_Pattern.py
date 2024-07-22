"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Solution:
Time Complexity: O(N)
Space Complexity: O(N)

"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        if len(pattern) == len(s.split(' ')):
            mapping = defaultdict(lambda: 0)
            revised_s = list()
            s = s.split(' ')

            for i in range(len(pattern)):
                if pattern[i] not in mapping and s[i] not in mapping.values():
                    mapping[pattern[i]] = s[i]
                revised_s.append(str(mapping[pattern[i]]))

            return True if revised_s == s else False
        else:
            return False
