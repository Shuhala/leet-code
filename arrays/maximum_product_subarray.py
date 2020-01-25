from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        c_min = c_max = result = nums[0]

        for i in range(1, len(nums)):
            tmp_max = c_max
            c_max = max(c_max * nums[i], c_min * nums[i], nums[i])
            c_min = min(tmp_max * nums[i], c_min * nums[i], nums[i])

            result = max(result, c_max)

        return result


solution = Solution()
assert 6 == solution.maxProduct([2, 3, -2, 4])
assert 0 == solution.maxProduct([-2, 0, -1])
assert 48 == solution.maxProduct([2, 3, -2, -4])
