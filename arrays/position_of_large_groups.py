from typing import List


class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        if len(S) < 3:
            return []

        large_groups = []
        streak = 1
        for i in range(1, len(S)):
            if S[i] == S[i - 1]:
                streak += 1
                if streak == 3:
                    # group found, append index of beginning
                    large_groups.append([i - 2])
                if i == len(S) - 1 and streak >= 3:
                    # end of list (would be skipped because we set the end index at the i + 1 char)
                    large_groups[-1].append(i)
            else:
                if streak >= 3 and len(large_groups) > 0:
                    # group exists and we reset the streak. add index of previous character
                    large_groups[-1].append(i - 1)
                streak = 1

        return large_groups


solution = Solution()
assert [[3, 6]] == solution.largeGroupPositions("abbxxxxzzy")
assert [] == solution.largeGroupPositions("abc")
assert [] == solution.largeGroupPositions("")
assert [[0, 2]] == solution.largeGroupPositions("aaa")
assert [[1, 3]] == solution.largeGroupPositions("baaa")
assert [[3, 5], [6, 9], [12, 14]] == solution.largeGroupPositions("abcdddeeeeaabbbcd")
