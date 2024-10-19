"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Solution:
Time Complexity: O(N)
Space Complexity: O(N)

"""

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        count = {}

        for num in arr:
            count[num] = arr.count(num)

        values = set(count.values())

        return len(count) == len(values)
      
