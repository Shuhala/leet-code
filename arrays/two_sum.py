from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return [-1, -1]

        complements = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in complements:
                return [complements[complement], i]
            else:
                complements[nums[i]] = i

        return [-1, -1]

    def twoSum_1(self, nums, target):
        for i, num in enumerate(nums):
            for j in range(len(nums)):
                if (num + nums[j]) == target and (i != j):
                    return i, j

    def twoSum_2(self, nums, target):
        ilist = []

        def valid_sum(n):
            return n + nums[i] == target and (nums.index(n) != i or nums.count(nums[i]) > 1)

        for i in range(len(nums)):
            res = [i for n in nums if valid_sum(n)]
            if res:
                ilist.append(i)

        return ilist


solution = Solution()
assert [0, 1] == solution.twoSum([2, 7, 11, 15], 9)
assert [0, 2] == solution.twoSum([-3, 4, 3, 90], 0)
