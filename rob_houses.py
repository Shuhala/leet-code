from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0

        if len(nums) < 2:
            return nums[0]

        money_values = [0 for _ in range(len(nums))]
        money_values[0] = nums[0]
        money_values[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            money_values[i] = max(money_values[i - 2] + nums[i], money_values[i - 1])

        return money_values[-1]


solution = Solution()
assert 4 == solution.rob([1, 2, 3])
assert 4 == solution.rob([1, 2, 3, 1])
assert 12 == solution.rob([2, 7, 9, 3, 1])
assert 4 == solution.rob([2, 1, 1, 2])
assert 7 == solution.rob([2, 1, 1, 5, 2])
assert 7 == solution.rob([1, 2, 1, 1, 5, 2])
