from collections import defaultdict
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        max_size = float('inf')
        dp = defaultdict(lambda: max_size)
        dp[0] = 0

        for i in range(1, amount + 1):
            dp[i] = 1 + min([dp[i - c] for c in coins])

        return dp[amount] if dp[amount] != max_size else -1


solution = Solution()
assert 3 == solution.coinChange([1, 2, 5], 11)
assert -1 == solution.coinChange([2], 3)
assert -1 == solution.coinChange([4, 5, 6], 3)
