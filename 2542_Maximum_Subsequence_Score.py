"""
You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and a positive integer k. You must choose a subsequence of indices from nums1 of length k.

For chosen indices i0, i1, ..., ik - 1, your score is defined as:

The sum of the selected elements from nums1 multiplied with the minimum of the selected elements from nums2.
It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).
Return the maximum possible score.

A subsequence of indices of an array is a set that can be derived from the set {0, 1, ..., n-1} by deleting some or no elements.

Solution:
Time Complexity: O(NLogN)
Space Complexity: O(N)

"""

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:

        nums = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        nums = sorted(nums, key = lambda x: x[1], reverse=True)

        minHeap = []
        n1sum = 0
        res = 0

        for n1, n2 in nums:
            n1sum += n1
            heapq.heappush(minHeap, n1)

            if len(minHeap) > k:
                n1pop = heapq.heappop(minHeap)
                n1sum -= n1pop
            
            if len(minHeap) == k:
                res = max(res, n1sum * n2)

        return res
