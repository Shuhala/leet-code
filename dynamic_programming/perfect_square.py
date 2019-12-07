class Solution:
    def numSquares(self, n: int) -> int:
        perfect_squares = [i for i in range(n + 1)]
        perfect_squares[0] = 0
        perfect_squares[1] = 1

        for i in range(1, n + 1):
            j = 1
            while j * j < i + 1:
                perfect_squares[i] = min(perfect_squares[i - j * j] + 1, perfect_squares[i])
                j += 1

        return perfect_squares[n]


solution = Solution()
assert 3 == solution.numSquares(12)
assert 2 == solution.numSquares(13)
