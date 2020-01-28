# 14. Longest Common Prefix
# Easy

# 1943

# 1634

# Add to List

# Share
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:

# All given inputs are in lowercase letters a-z.

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = list(zip(*strs))

        prefix = ''
        for i in l:
            if len(set(i)) == 1:
                prefix += i[0]
            else:
                break
        return prefix


x = Solution()
print(x.longestCommonPrefix(["flower", "flow", "flight"]))
