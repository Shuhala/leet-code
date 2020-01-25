from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) < 1:
            return 0
        if len(matrix[0]) < 1:
            return 0

        dp = [0 for _ in range(len(matrix[0]))]
        max_rect = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if int(matrix[i][j]) == 1:
                    dp[j] = dp[j] + 1

            max_val = 0
            for j in range(len(dp)):
                if dp[j] == 0:
                    continue
                k = j + 1
                while k < len(dp):
                    if dp[k] == 0:
                        break
                    k += 1
                    if (k - j) * min(dp[j:k]) > max_val:
                        max_val = (k - j) * min(dp[j:k])

            max_rect = max(*dp, max_val, max_rect)

        return max_rect


solution = Solution()
assert 6 == solution.maximalRectangle(
    [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
)
assert 1 == solution.maximalRectangle([["0", "1"], ["1", "0"]])
