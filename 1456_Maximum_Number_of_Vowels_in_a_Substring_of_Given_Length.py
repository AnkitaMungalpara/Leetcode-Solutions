"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Solution:
Time Complexity: O(N)
Space Complexity: O(1)

"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        count = 0

        for i in range(k):
            count += int(s[i] in vowels)
        res = count

        for i in range(k, len(s)):
            count += int(s[i] in vowels)
            count -= int(s[i-k] in vowels)
            res = max(res, count)
        
        return res
      
