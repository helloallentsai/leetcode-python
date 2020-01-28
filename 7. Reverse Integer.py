# 7. Reverse Integer
# Easy

# 2791

# 4370

# Add to List

# Share
# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg = True

        x = abs(x)
        result = 0
        while (x > 0):
            digit = x % 10
            result = result * 10 + digit
            x = x // 10

        if neg:
            result *= -1

        if (-2)**31 <= result <= 2**31 - 1:
            return result
        else:
            return 0


x = Solution()
print(x.reverse(120))
