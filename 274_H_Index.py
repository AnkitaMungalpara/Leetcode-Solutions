"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: 
The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

Solution:
Time Complexity: O(N)
Space Complexity: O(N)

"""

class Solution:
    def hIndex(self, citations: List[int]) -> int:

        # Method 1
        sorted_citations = sorted(citations, reverse=True)
        i = 0
        while i < len(citations) and sorted_citations[i] > i :
            i += 1
            continue
        return i

        # Method 2
        n = len(citations)
        count = [0] * (n+1)

        for c in citations:
            count[min(c, n)] += 1

        index = 0
        for i, c in reversed(list(enumerate(count))):
            index += c
            if index >= i:
                return i
    
