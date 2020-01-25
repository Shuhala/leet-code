from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 1:
            return ""
        if len(strs) == 1:
            return strs[0]

        common_prefix = ""
        for i in range(min(len(s) for s in strs)):
            char = strs[0][i]
            if all(s[i] == char for s in strs):
                common_prefix += char
            else:
                break

        return common_prefix


solution = Solution()
assert "fl" == solution.longestCommonPrefix(["flower", "flow", "flight"])
assert "" == solution.longestCommonPrefix(["dog", "racecar", "car"])
assert "" == solution.longestCommonPrefix([])
assert "c" == solution.longestCommonPrefix(["c","c"])
