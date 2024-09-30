"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Solution:
Time Complexity: O(N)
Space Complexity: O(N)

"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        max_streak = 0
        num_set = set(nums)

        for num in nums:
            if num - 1 not in num_set:
                curr = num
                curr_streak = 1

                while curr + 1 in num_set:
                    curr += 1
                    curr_streak += 1

                max_streak = max(max_streak, curr_streak)

        return max_streak
        
