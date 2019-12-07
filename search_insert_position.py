from typing import List


class Solution:
    """
    Given a sorted array and a target value, return the index if the target is found.
    If not, return the index where it would be if it were inserted in order.
    """

    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) < 1:
            return 0

        i = 0
        j = len(nums)
        mid = 0

        while j > i + 1:
            mid = (i + j) // 2
            if target == nums[mid]:
                return mid
            elif nums[mid] < target:
                i = mid
            elif nums[mid] > target:
                j = mid

        if nums[i] >= target:
            return i
        if nums[j - 1] < target:
            return j

        return mid


solution = Solution()
assert 2 == solution.searchInsert([1, 3, 5, 6], 5)
assert 1 == solution.searchInsert([1, 3, 5, 6], 2)
assert 4 == solution.searchInsert([1, 3, 5, 6], 7)
assert 0 == solution.searchInsert([1, 3, 5, 6], 0)
assert 0 == solution.searchInsert([], 0)
assert 1 == solution.searchInsert([1, 3], 2)
assert 0 == solution.searchInsert([1, 3], 1)
