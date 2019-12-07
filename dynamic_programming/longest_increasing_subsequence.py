import bisect
import sys
from typing import List

import big_o

from utils import estimate_big_o


class Solution:
    """
    Given an unsorted array of integers, find the length of longest increasing subsequence.
    """

    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Time complexity: O(n^2)
        Space complexity: O(n)
        """
        if len(nums) < 1:
            return 0

        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            max_val = float('-inf')
            for j in range(i):
                if nums[j] < nums[i] and dp[j] >= max_val:
                    max_val = dp[j] + 1
                    dp[i] = max_val

        return max(dp)

    def lengthOfLISBisect(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [sys.maxsize] * len(nums)
        for x in nums:
            # insert in sorted position
            dp[bisect.bisect_left(dp, x)] = x

        # get position of biggest element
        return bisect.bisect(dp, max(nums))


solution = Solution()
assert 4 == solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
assert 4 == solution.lengthOfLIS([10, 1, 2, 5, 12, 4])
assert 2 == solution.lengthOfLIS([-2, -1])
assert 6 == solution.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6])

estimate_big_o(solution.lengthOfLIS, big_o.datagen.range_n)
# estimate_big_o(solution.lengthOfLISBisect, big_o.datagen.range_n)
