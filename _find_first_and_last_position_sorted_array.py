from typing import List

import big_o

from utils import estimate_big_o


class Solution:
    def edge_index(self, nums, target, left):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid + 1

        return lo

    def searchRange(self, nums: List[int], target: int = 20) -> List[int]:
        if len(nums) < 1:
            return [-1, -1]

        left = self.edge_index(nums, target, True)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]

        right = self.edge_index(nums, target, False)

        return [left, right - 1]

    def searchRange2(self, nums: List[int], target: int = 20) -> List[int]:
        if len(nums) < 1:
            return [-1, -1]
        if len(nums) == 1:
            return [0, 0] if target in nums else [-1, -1]

        i = 0
        j = len(nums)
        mid = 0

        # find target index
        while i < j - 1:
            if nums[mid] == target:
                break
            mid = (i + j) // 2
            if target > nums[mid]:
                i = mid
            else:
                j = mid

        if nums[mid] != target:
            return [-1, -1]

        # move i and j to find extremities
        i = j = mid
        while i > 0 and nums[i - 1] == target:
            i -= 1
        while j < len(nums) - 1 and nums[j + 1] == target:
            j += 1

        return [i, j]


solution = Solution()
assert [2, 4] == solution.searchRange([1, 2, 5, 5, 5, 9], 5)
assert [3, 4] == solution.searchRange([5, 7, 7, 8, 8, 10], 8)
assert [-1, -1] == solution.searchRange([5, 7, 7, 8, 8, 10], 6)
assert [0, 0] == solution.searchRange([5], 5)
assert [0, 1] == solution.searchRange([5, 5], 5)
assert [-1, -1] == solution.searchRange([], 5)
assert [0, 0] == solution.searchRange([1, 3], 1)
assert [1, 1] == solution.searchRange([1, 3], 3)
assert [-1, -1] == solution.searchRange([2, 2], 3)
assert [1, 2] == solution.searchRange([1, 2, 2], 2)

generator = lambda n: big_o.datagen.range_n(n, 10)
estimate_big_o(solution.searchRange, big_o.datagen.range_n)
estimate_big_o(solution.searchRange2, big_o.datagen.range_n)
