from typing import List

import big_o

from utils import estimate_big_o


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return 0
        if len(cost) == 1:
            return 0

        dp = [c for c in cost]
        dp.append(0)

        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 1] + dp[i], dp[i - 2] + dp[i])

        return dp[len(cost)]


solution = Solution()
assert 15 == solution.minCostClimbingStairs([10, 15, 20])
assert 6 == solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])

estimate_big_o(solution.minCostClimbingStairs, big_o.datagen.range_n)
