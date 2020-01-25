from heapq import heappop, heappush


class Solution:
    # Time complexity: O(r * c * k).
    # Space complexity: O(r * c * k).
    def shortestPathBreakWalls(self, matrix, k):
        m, n = len(matrix), len(matrix[0])
        # allowed moves
        offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # elements in form of: (path length, wall breaks, (row, column))
        pq = [(0, 0, (0, 0))]

        # store visited states: (wall breaks, (row, column))
        seen = {(0, (0, 0))}

        while pq:
            # pick the current shortest path
            # pick one with fewest wall breaks, if there is a tie
            length, wall_breaks, (row, col) = heappop(pq)
            for direction_row, direction_col in offsets:
                current_row, current_col = row + direction_row, col + direction_col
                # skip if out of bound
                if not (0 <= current_row < m and 0 <= current_col < n):
                    continue

                kk = wall_breaks + matrix[current_row][current_col]

                # skip if exceed wall break limit or state has been visited
                if kk > k or (kk, (current_row, current_col)) in seen:
                    continue

                seen.add((kk, (current_row, current_col)))

                # reach target
                if (current_row, current_col) == (m - 1, n - 1):
                    return length + 1

                heappush(pq, (length + 1, kk, (current_row, current_col)))

        return -1


solution = Solution()

assert 7 == solution.shortestPathBreakWalls(
    [[0, 1, 0, 0, 0],
     [0, 0, 0, 1, 0],
     [1, 1, 0, 1, 0],
     [1, 1, 1, 1, 0]],
    1
)
# assert -1 == solution.shortestPathBreakWalls(
#     [[0, 1, 1],
#      [1, 1, 0],
#      [1, 1, 0]],
#     1
# )
