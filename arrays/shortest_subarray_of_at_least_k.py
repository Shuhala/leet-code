import collections
from typing import List


class Solution(object):
    def shortestSubarray(self, A: List[int], K: int) -> int:
        size = len(A)
        # add 0 first position
        current_list = [0]
        for num in A:
            # current sum at index..
            # [1,2,3] -> [0,1,3,6]
            current_list.append(current_list[-1] + num)

        # Want smallest y-x with Py - Px >= K
        ans = size + 1  # N+1 is impossible
        # queue of indices
        queue = collections.deque()  # opt(y) candidates, represented as indices of P
        for i, current_sum in enumerate(current_list):
            # if current_sum is smaller or equal to the last element in our queue, pop right
            # we only need to consider increasing sequences of current_list[x] to find candidates x for opt(y)
            while queue and current_sum <= current_list[queue[-1]]:
                queue.pop()

            # We have an answer of at least K
            # current_sum - first element in our queue
            while queue and current_sum - current_list[queue[0]] >= K:
                # get min length between current answer and what we just found
                # (we pop the first index in the queue, such as each index is increasing)
                ans = min(ans, i - queue.popleft())

            # add index
            queue.append(i)

        return ans if ans < size + 1 else -1


solution = Solution()
assert 1 == solution.shortestSubarray([1], 1)
assert -1 == solution.shortestSubarray([1, 2], 4)
assert 3 == solution.shortestSubarray([2, -1, 2], 3)
assert 1 == solution.shortestSubarray([1, 2, 3], 3)
assert 3 == solution.shortestSubarray([84, -37, 32, 40, 95], 167)
