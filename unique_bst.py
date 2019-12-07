import math


class Solution:
    def numTrees(self, n: int) -> int:
        return int(math.factorial(2 * n) / (math.factorial(n + 1) * math.factorial(n)))


solution = Solution()
assert 5 == solution.numTrees(3)
