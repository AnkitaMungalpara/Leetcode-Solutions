"""
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

Solution:
Time Complexity: O(N)
Space Complexity: O(N)

"""

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        res1 = set([num for num in nums1 if num not in nums2])
        res2 = set([num for num in nums2 if num not in nums1])

        return list(res1), list(res2)
      
