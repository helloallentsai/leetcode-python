# 53. Maximum Subarray
# Easy

# 6193

# 262

# Add to List

# Share
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev = 0
        max_sum = float('-inf')
        for i in range(len(nums)):
            prev = max(prev+nums[i], nums[i])
            max_sum = max(max_sum, prev)
        return max_sum
