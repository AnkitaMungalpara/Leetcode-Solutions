"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

Solution:
Time Complexity: O(N)
Space Complexity: O(1)

"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        # Method 1:
        for i in range(len(nums)):
            left_sum  = sum(nums[:i])
            right_sum = sum(nums[i+1:])
            
            if left_sum == right_sum:
                return i

        return -1

        # Method 2:
        S = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            if left_sum == (S - left_sum - num):
                return i
            left_sum += num

        return -1
        
