"""
You are given an integer array nums. 
You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Solution:
Time Complexity: O(N)
Space Complexity: O(1)

"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        total_steps = len(nums) - 1
        for i in range(len(nums)- 1, -1, -1):
            if nums[i] + i >= total_steps:
                total_steps = i
                
        return True if total_steps == 0 else False