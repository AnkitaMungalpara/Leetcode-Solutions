"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Solution:
Time Complexity: O(N^2)
Space Complexity: O(N^2)

"""

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        d = {}
        n = len(grid)
        res = 0 

        for i in grid:
            if tuple(i) not in d:
                d[tuple(i)] = 1
            else:
                d[tuple(i)] += 1

        for c in range(n):
            col = [grid[i][c] for i in range(n)]
            if tuple(col) in d:
                res += d[tuple(col)]

        return res
