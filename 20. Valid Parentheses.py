# 20. Valid Parentheses
# Easy

# 4035

# 194

# Add to List

# Share
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:

# Input: "()"
# Output: true
# Example 2:

# Input: "()[]{}"
# Output: true
# Example 3:

# Input: "(]"
# Output: false
# Example 4:

# Input: "([)]"
# Output: false
# Example 5:

# Input: "{[]}"
# Output: true


class Solution:
    def isValid(self, s: str) -> bool:
        map = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for letter in s:
            if letter in map.keys():
                stack.append(letter)
            else:
                if len(stack) == 0:
                    return False
                if map[stack.pop()] != letter:
                    return False
        return not len(stack)


x = Solution()
print(x.isValid('{[}'))
