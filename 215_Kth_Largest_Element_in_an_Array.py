"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Solution:
Time Complexity: O(NLogK)
Space Complexity: O(K)

"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # min-heap 
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
              
        return heap[0]
