"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Solution:
Time Complexity: O(N)
Space Complexity: O(1)

"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        i, j = 0, 0
        size = set()
        total = 0

        while i < len(nums) and j < len(nums) and i <= j:
            total += nums[j]

            if total < target:
                j += 1
                
            elif total >= target:
                length = (j-i) + 1
                size.add(length)
                total -= (nums[i] + nums[j])
                i += 1
        
        return min(size) if len(size) > 0 else 0
      
