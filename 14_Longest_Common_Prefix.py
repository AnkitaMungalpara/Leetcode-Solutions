"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Solution:
Time Complexity: O(N*M)
Space Complexity: O(1)

"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        pre = strs[0]

        for i in range(1, len(strs)):
            while strs[i].find(pre) != 0:
                pre = pre[0:len(pre) - 1]
                if pre == "":
                    return ""
                    
        return pre
        