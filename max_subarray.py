import sys
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_value = sys.maxsize * -1
        current_max = 0

        for i in range(len(nums)):
            current_max += nums[i]
            if current_max > max_value:
                max_value = current_max
            if current_max < 0:
                current_max = 0

        return max_value


solution = Solution()
assert 6 == solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
assert -1 == solution.maxSubArray([-2, -1, -3, -4, -1, -2, -1, -5, -4])
