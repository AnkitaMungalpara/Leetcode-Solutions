"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Solution:
Time Complexity: O(N!)
Space Complexity: O(N)

"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []

        def backtrack(curr):
            if len(curr) == len(nums):
                result.append(curr[:])
                return

            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()                   
        
        backtrack([])
        
        return result
