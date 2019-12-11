from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] == 1:
            return 0
        if len(obstacleGrid) == 1:
            # only 1 row, assert there's no obstacle in it
            return 0 if 1 in obstacleGrid[0] else 1

        # init first cell
        obstacleGrid[0][0] = 1

        # init first col
        for i in range(1, len(obstacleGrid)):
            # current value is not an obstacle AND previous has a path
            obstacleGrid[i][0] = 1 if obstacleGrid[i][0] == 0 and obstacleGrid[i - 1][0] == 1 else 0

        # init first row
        for j in range(1, len(obstacleGrid[0])):
            # current value is not an obstacle and previous has a path
            obstacleGrid[0][j] = 1 if obstacleGrid[0][j] == 0 and obstacleGrid[0][j - 1] == 1 else 0

        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[i])):
                # if current is not an obstacle, top + left value
                obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1] if obstacleGrid[i][j] == 0 else 0

        return obstacleGrid[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]


solution = Solution()
assert 2 == solution.uniquePathsWithObstacles([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
])
assert 0 == solution.uniquePathsWithObstacles([
    [0, 0, 0],
    [1, 1, 1],
    [0, 0, 0]
])
assert 1 == solution.uniquePathsWithObstacles([[0]])
assert 1 == solution.uniquePathsWithObstacles([[0], [0]])
