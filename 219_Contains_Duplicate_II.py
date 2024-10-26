"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Solution:
Time Complexity: O(N)
Space Complexity: O(N)

"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        hashMap = {}
        for i, num in enumerate(nums):
            if num in hashMap and abs(hashMap[num] - i) <= k:
                return True
            else:
                hashMap[num] = i
        
        return False
      
