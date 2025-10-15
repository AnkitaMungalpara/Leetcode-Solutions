"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

1 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].


Solution:
Time Complexity: O(4^N)
Space Complexity: O(N)

"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []

        digitsToChar = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def backtrack(i, cur_str):
            if len(cur_str) == len(digits):
                res.append(cur_str)
                return

            for c in  digitsToChar[digits[i]]:
                backtrack(i+1, cur_str + c)

        if digits:
            backtrack(0, "")

        return res
      
