import collections
import itertools
from collections import defaultdict
from typing import List


class Solution:
    def twoSums(self, nums, target, index):
        results = []
        compl = []
        for i in range(len(nums)):
            if i != index:
                complement = target - nums[i]
                if complement in compl:
                    results.append([complement, nums[i]])

                compl.append(nums[i])

        return results

    def combinations(self, nums):
        combinations = defaultdict(list)
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if j != i:
                    combinations[nums[i] + nums[j]].append((i, j))

        return combinations

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        """
        Questions:
            - What if multiple results possible with the same number?
            - Answer is in the right half of the array
        Optimisations:
            - Has to equal 0, so sort the list, and break if > 0
            - Compute combinations at the start?
        """
        if len(nums) < 3:
            return []

        nums = sorted(nums)
        combinations = self.combinations(nums)
        solutions = []
        solution_sets = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break

            goal = 0 - nums[i]
            if goal in combinations:
                for pair in combinations[goal]:
                    if i not in pair:
                        sol = [nums[pair[0]], nums[pair[1]], nums[i]]
                        if set(sol) not in solution_sets:
                            solutions.append(sol)
                        solution_sets.append(set(sol))

        return solutions

    def threeSum3(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        res = []
        for t in itertools.combinations(nums, 3):
            if sum(t) == 0:
                c = collections.Counter(t)
                if c not in res:
                    res.append(c)
        return [list(t.elements()) for t in res]

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        values = set()
        solutions = []
        solution_sets = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                goal = -(nums[i] + nums[j])
                if goal in values:
                    sol = [goal, nums[i], nums[j]]
                    if set(sol) not in solution_sets:
                        solutions.append(sol)
                        solution_sets.append(set(sol))
                else:
                    values.add(nums[j])

        return solutions


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
