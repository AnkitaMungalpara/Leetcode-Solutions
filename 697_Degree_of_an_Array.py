"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Solution:
Time Complexity: O(N)
Space Complexity: O(N)

"""

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        left, right, count = {}, {}, {}
        
        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            right[num] = i
            count[num] = count.get(num, 0) + 1

        subarr_size = len(nums)
        degree = max(count.values())

        for c in count:
            if count[c] == degree:
                subarr_size = min(right[c] - left[c] + 1, subarr_size)

        return subarr_size
