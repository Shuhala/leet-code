from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 1:
            return 0

        buy = prices[0]
        profit = 0

        for sell in prices:
            profit = max(profit, sell - buy)
            buy = min(buy, sell)

        return profit


solution = Solution()
assert 5 == solution.maxProfit([7, 1, 5, 3, 6, 4])
assert 0 == solution.maxProfit([7, 6, 4, 3, 1])
