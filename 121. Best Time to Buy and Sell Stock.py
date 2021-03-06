# 121. Best Time to Buy and Sell Stock
# Easy

# 3811

# 171

# Add to List

# Share
# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

# Example 1:

# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:

# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
# Accepted
# 697,247
# Submissions
# 1,418,568

from typing import List
from math import inf


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_num = inf
        max_num = 0
        for price in prices:
            min_num = min(price, min_num)
            max_num = max(price - min_num, max_num)

        return max_num


x = Solution()
print(x.maxProfit([7, 3, 5, 1, 6, 4]))
