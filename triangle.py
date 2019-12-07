from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0 for _ in range(len(triangle))]

        dp[0] = triangle[0][0]

        for i in range(len(triangle)):
            for j in range(len(triangle[i])):
                dp[i] = min(dp[i] + dp[i - 1])


solution = Solution()
assert 11 == solution.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
assert 8 == solution.minimumTotal([[-1], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
assert 14 == solution.minimumTotal([[1], [3, 4], [6, 5, 23], [4, 9, 8, 3]])

# [
#      [2],     0
#     [3,4],    1
#    [6,5,7],   2
#   [4,1,8,3]   3
#  [1,4,1,8,3]  4
# ]
