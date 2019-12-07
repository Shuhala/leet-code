from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) < 1:
            return -1
        if len(nums) < 3:
            return nums.index(target) if target in nums else -1

        lo, hi, mid = 0, len(nums) - 1, 0

        while lo < hi - 1:
            mid = lo + (hi - lo) // 2
            if target == nums[mid]:
                return mid
            if target == nums[lo]:
                return lo
            if target == nums[hi]:
                return hi

            # pivot on the left side
            if nums[lo] > nums[mid] and nums[hi] > nums[mid]:
                if nums[mid] < target < nums[hi]:
                    lo = mid
                else:
                    hi = mid
            # pivot on the right side
            elif nums[hi] < nums[mid] and nums[lo] < nums[mid]:
                if nums[lo] < target < nums[mid]:
                    hi = mid
                else:
                    lo = mid
            # on the pivot
            else:
                if nums[hi] > target > nums[mid]:
                    lo = mid
                else:
                    hi = mid

        return -1


solution = Solution()
assert 4 == solution.search([4, 5, 6, 7, 0, 1, 2], 0)
assert -1 == solution.search([4, 5, 6, 7, 0, 1, 2], 3)
assert 0 == solution.search([1], 1)
assert -1 == solution.search([1], 0)
assert 0 == solution.search([1, 3, 5, 2], 1)
assert 5 == solution.search([4, 5, 6, 7, 0, 1, 2], 1)
assert 4 == solution.search([4, 5, 6, 7, 8, 1, 2, 3], 8)
