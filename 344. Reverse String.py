# 344. Reverse String
# Easy

# 1032

# 617

# Add to List

# Share
# Write a function that reverses a string. The input string is given as an array of characters char[].

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# You may assume all the characters consist of printable ascii characters.


# Example 1:

# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s)-1
        while(left < right):
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s


test = Solution()
print(test.reverseString(["H", "a", "n", "n", "a", "h"]))
