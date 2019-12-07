class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1

        dp = [i for i in range(1, n + 1)]
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n - 1]


solution = Solution()
assert 1 == solution.climbStairs(-5)
assert 1 == solution.climbStairs(0)
assert 1 == solution.climbStairs(1)
assert 2 == solution.climbStairs(2)
assert 3 == solution.climbStairs(3)
assert 8 == solution.climbStairs(5)
assert 28657 == solution.climbStairs(22)
