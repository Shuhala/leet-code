from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return -1

        lo, hi, mid = 0, len(nums) - 1, 0
        while lo < hi - 1:
            mid = lo + (hi - lo) // 2
            if nums[lo] > nums[mid] and nums[hi] > nums[mid]:
                hi = mid
            elif nums[lo] < nums[mid] and nums[hi] < nums[mid]:
                lo = mid
            else:
                break

        if nums[mid] < nums[lo] and nums[mid] < nums[hi]:
            return nums[mid]
        elif nums[lo] < nums[hi]:
            return nums[lo]

        return nums[hi]


solution = Solution()
assert 1 == solution.findMin([3, 4, 5, 1, 2])
assert 0 == solution.findMin([4, 5, 6, 7, 0, 1, 2])
assert 0 == solution.findMin([0, 1])
assert 0 == solution.findMin([1, 0])
assert 1 == solution.findMin([1])
