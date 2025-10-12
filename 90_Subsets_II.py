"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.


Solution:
Time Complexity: O(N*2^N)
Space Complexity: O(N)

"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        result = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                result.append(subset[::])
                return

            # add element at nums[i]
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()

            # do not add element at nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            backtrack(i+1, subset)
        
        backtrack(0, [])

        return result

        
