from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()
        for i in range(len(matrix)):
            if 0 in matrix[i]:
                rows.add(i)
                cols.update([j for j, value in enumerate(matrix[i]) if value == 0])

        for row in rows:
            for j in range(len(matrix[row])):
                matrix[row][j] = 0

        for col in cols:
            for i in range(len(matrix)):
                matrix[i][col] = 0


solution = Solution()
solution.setZeroes([
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
])
