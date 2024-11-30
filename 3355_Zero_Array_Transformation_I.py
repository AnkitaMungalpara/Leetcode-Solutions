"""
You are given an integer array nums of length n and a 2D array queries, where queries[i] = [li, ri].

For each queries[i]:

Select a subset of indices within the range [li, ri] in nums.
Decrement the values at the selected indices by 1.
A Zero Array is an array where all elements are equal to 0.

Return true if it is possible to transform nums into a Zero Array after processing all the queries sequentially, otherwise return false.

Solution:
Time Complexity: O(N+Q)
Space Complexity: O(N)

"""

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:

        line = [0 for i in range(len(nums) + 1)]

        for l, r in queries:
            line[l] += 1
            line[r+1] -= 1

        for i in range(1, len(line)):
            line[i] += line[i-1]

        for i in range(len(nums)):
            if line[i] < nums[i]:
                return False

        return True
