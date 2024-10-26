"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Solution:
Time Complexity: O(N)
Space Complexity: O(1)

"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sub = nums[0]
        cur_sum = 0

        for n in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += n
            max_sub = max(max_sub, cur_sum)
        
        return max_sub
