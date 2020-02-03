# 412. Fizz Buzz
# Easy

# 693

# 989

# Add to List

# Share
# Write a program that outputs the string representation of numbers from 1 to n.

# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

# Example:

# n = 15,

# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        count = 1
        while count <= n:
            if count % 3 == 0 and count % 5 == 0:
                string = 'FizzBuzz'
            elif count % 3 == 0:
                string = 'Fizz'
            elif count % 5 == 0:
                string = 'Buzz'
            else:
                string = str(count)

            result.append(string)
            count += 1

        return result


x = Solution()
print(x.fizzBuzz(15))
