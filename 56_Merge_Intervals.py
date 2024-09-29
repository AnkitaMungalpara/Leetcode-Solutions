"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Solution:
Time Complexity: O(NLogN)
Space Complexity: O(N)

"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda x: x[0])
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if start <= result[-1][1]:
                result[-1][1] = max(end, result[-1][1])
            elif start > result[-1][1]:
                result.append([start, end])
        
        return result
