a1 = [1, 2]
a2 = [2, 4]


class Solution(object):
    @staticmethod
    def merge(nums1, m, nums2, n):
        nums1 = nums1[0:m] + nums2[0:n]

        return nums1

print(Solution.merge(a1, 0, a2, 1))
