"""
Given a string s, return the longest palindromic substring in s.

Solution:
Time Complexity: O(N^3)
Space Complexity: O(N)

"""

class Solution:
    def longestPalindrome(self, s: str) -> str:

        result = []
        count = 0
        for i in range(len(s)):
            if s[i] not in result and len(s[i]) > count:
                result.append(s[i])
                count = len(s[i])
            j = 0
            while j <= i:
                sub = s[j:i+1]
                if sub == sub[::-1]:
                    if sub not in result and len(sub) > count:
                        result.append(sub)
                        count = len(sub)
                        break
                j+=1
        
        return result[-1]
      
