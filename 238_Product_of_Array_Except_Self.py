"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Solution:
Time Complexity: O(N)
Space Complexity: O(1)

"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre, post = 1, 1
        result = [1] * len(nums)

        for i in range(1, len(nums)):
            result[i] = pre * nums[i-1]
            pre = result[i]

        for i in range(len(nums)-1, -1, -1):
            result[i] = post * result[i]
            post *= nums[i]

        return result
