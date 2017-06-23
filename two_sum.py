s = [2, 5, 3, 15]
t = 20


class Solution(object):
    @staticmethod
    def twoSum(nums, target):
        for i, num in enumerate(nums):
            for j in range(len(nums)):
                if (num + nums[j]) == target and (i != j):
                    return i, j

    @staticmethod
    def twoSum2(nums, target):
        ilist = []

        def valid_sum(n):
            return n+nums[i] == target and (nums.index(n) != i or nums.count(nums[i]) > 1)

        for i in range(len(nums)):
            res = [i for n in nums if valid_sum(n)]
            if res:
                ilist.append(i)

        return ilist


print(Solution.twoSum(s, t))
