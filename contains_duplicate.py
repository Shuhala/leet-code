array = [1, 2, 15, 6, 3, 7, 2]


class Solution(object):
    @staticmethod
    def containsDuplicate(nums):
        for num in nums:
            if nums.count(num) > 1:
                return True
        return False

    @staticmethod
    def containsDuplicate2(nums):
        print(nums)
        print(set(nums))
        return len(nums) != len(set(nums))
        # set cannot contain duplicates, it'll merge them


print(Solution.containsDuplicate2(array))
