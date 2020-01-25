from collections import Counter
from typing import List


class Solution:
    """
    Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
    You may assume that the array is non-empty and the majority element always exist in the array.
    """

    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common(1)[0][0]


solution = Solution()
assert 3 == solution.majorityElement([3, 2, 3])
assert 2 == solution.majorityElement([2, 2, 1, 1, 1, 2, 2])
