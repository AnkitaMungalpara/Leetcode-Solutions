"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. 
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Solution:
Time Complexity: O(N)
Space Complexity: O(1)

"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        left, right = 0, 0

        while right < len(nums):
            count = 1
            while right + 1 < len(nums) and nums[right] == nums[right+1]:
                right += 1
                count += 1
            
            for i in range(min(2, count)):
                nums[left] = nums[right]
                left += 1

            right += 1

        return left