"""
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element.
 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


Solution:
Time Complexity: O(N)
Space Complexity: O(1)

"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:

            if n == 0:
                curMin, curMax = 1, 1
                continue
            
            temp = curMax * n
            curMax = max(curMax * n, n * curMin, n)
            curMin = min(temp,  n * curMin, n)
            res = max(res, curMax)

        return res

      
