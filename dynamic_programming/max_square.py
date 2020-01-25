from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        Time complexity: O(mn)
        Space complexity : O(mn)O(mn)
        """
        if len(matrix) < 1:
            return 0
        if len(matrix[0]) < 1:
            return 0

        dp = [[] for _ in range(len(matrix) + 1)]
        for i in range(len(dp)):
            dp[i] = [0 for _ in range(len(matrix[0]) + 1)]

        max_square = 0
        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                if int(matrix[i - 1][j - 1]) == 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + int(matrix[i - 1][j - 1])
                    if dp[i][j] > max_square:
                        max_square = dp[i][j]

        return max_square * max_square


solution = Solution()
assert 4 == solution.maximalSquare(
    [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
)
assert 4 == solution.maximalSquare(
    [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["1", "0", "0", "0", "0"], ["1", "0", "0", "1", "0"]]
)
