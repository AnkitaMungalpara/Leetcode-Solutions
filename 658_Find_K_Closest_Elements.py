"""
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b

Solution:
Time Complexity: O(NLog(N)+KLog(N))
Space Complexity: O(N)

"""

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        q = []
        res = []
        
        for i, j in enumerate(arr):
            heapq.heappush(q, (abs(j-x), j))

        while k: 
            val = heapq.heappop(q)
            res.append(val[1])
            k -= 1
        
        return sorted(res)
      
