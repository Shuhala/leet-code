import collections
import itertools
from collections import defaultdict
from typing import List


class Solution:
    def combinations(self, nums):
        combinations = defaultdict(list)
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if j != i:
                    combinations[nums[i] + nums[j]].append((i, j))

        return combinations

    def threeSum2(self, nums: List[int], target=0) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        results = []

        # You can think of it as The last two have been tried by all others.
        for i in range(len(nums) - 2):
            if nums[i] > target:
                # We do not need to consider i after nums[i]>0, since sum of 3 positive will be always greater than zero
                break
            if i > target and nums[i] == nums[i - 1]:
                # If the number is the same as the number before, we have used it as target already, continue.
                continue

            # We always start the left pointer from i+1 because the combination of 0~i has already been tried
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                # If the total is less than target, we need it to be larger, so we move the left pointer.
                if total < target:
                    left += 1
                # If the total is greater than target, we need it to be smaller, so we move the right pointer.
                elif total > target:
                    right -= 1
                # If the total is target, bingo!
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    # We need to move the left and right pointers to the next different numbers,
                    # so we do not get repeating result.
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right += 1

        return results

    def threeSum(self, nums: List[int], target=0) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        results = []

        # You can think of it as The last two have been tried by all others.
        for i in range(len(nums) - 2):
            if nums[i] > target:
                # We do not need to consider i after nums[i]>0, since sum of 3 positive will be always greater than zero
                break
            if i > target and nums[i] == nums[i - 1]:
                # If the number is the same as the number before, we have used it as target already, continue.
                continue

            # We always start the left pointer from i+1 because the combination of 0~i has already been tried
            left = i + 1
            right = len(nums) - 1
            value = target - nums[i]

            while left < right:
                # found a complement
                if value == nums[left] + nums[right]:
                    results.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        # skip left duplicates
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        # skip right duplicates
                        right -= 1

                    left += 1
                    right -= 1
                elif nums[left] + nums[right] > value:
                    # value is too high
                    right -= 1
                else:
                    # value is too low
                    left += 1

        return results


def arrays_are_equal(a, b):
    a = [sorted(i) for i in a]
    b = [sorted(i) for i in b]
    return sorted(a) == sorted(b)


solution = Solution()
# assert arrays_are_equal([[-1, 0, 1], [-1, -1, 2]], solution.threeSum([-1, 0, 1, 2, -1, -4]))
assert arrays_are_equal([[0, -1, 1]], solution.threeSum([2, 2, 1, 0, -1, 1]))
assert arrays_are_equal([[-1, 1, 0]], solution.threeSum([0, -1, 1, 3, 2, 2]))
assert arrays_are_equal([], solution.threeSum([1, 2, -2, -1]))
assert arrays_are_equal(
    [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]],
    solution.threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6])
)
assert arrays_are_equal(
    [[-5, 1, 4], [-4, 0, 4], [-4, 1, 3], [-2, -2, 4], [-2, 1, 1], [0, 0, 0]],
    solution.threeSum([-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0])
)
