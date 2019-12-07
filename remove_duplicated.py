from typing import List

import big_o


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        items = set()
        length = len(nums)
        i = 0
        while i < length:
            if nums[i] not in items:
                items.add(nums[i])
                i += 1
            else:
                del nums[i]
                length -= 1

        return len(nums)


solution = Solution()
assert 2 == solution.removeDuplicates([1, 1, 2])
generator = lambda n: big_o.datagen.range_n(n, 1)
best, others = big_o.big_o(solution.removeDuplicates, generator)
print(best)
